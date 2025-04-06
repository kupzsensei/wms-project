from rest_framework import serializers
from .models import Transaction , TransactionProduct
from product.models import Product

class TransactionProductSerializer(serializers.ModelSerializer):
    subtotal = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = TransactionProduct
        fields = ['id' , 'transaction' , 'product', 'quantity','price', 'subtotal']
        extra_kwargs = {
            'transaction': {'read_only':True}
        }

    def get_subtotal(self, obj):
        return obj.subtotal

class TransactionListSerializer(serializers.ModelSerializer):
    transaction_items = TransactionProductSerializer(many=True , read_only=True)
    total = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)  # This matches the annotation

    class Meta:
        model = Transaction
        fields = [
            'id',
            'transaction_number',
            'transaction_type',
            'edited_by',
            'transaction_items',
            'created_at',
            'updated_at',
            'total'
        ]
        

class TransactionCreateSerializer(serializers.ModelSerializer):
    products = TransactionProductSerializer(many=True , write_only=True)
    class Meta:
        model = Transaction
        fields = "__all__"

    def create(self, validated_data):
        products = validated_data.pop('products')
        transaction = Transaction.objects.create(**validated_data)
        for product in products:
            print(product)
            # product_id = product['product']
            TransactionProduct.objects.create(transaction=transaction , **product)
        return transaction