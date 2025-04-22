from rest_framework import serializers
from .models import Transaction , TransactionProduct
from outlet.serializers import OutletSerializer
from product.serializers import ProductListSerializer

class TransactionProductSerializer(serializers.ModelSerializer):
    subtotal = serializers.SerializerMethodField(read_only=True)
    product = ProductListSerializer(read_only=True)
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
            'created_by',
            'outlet',
            'transaction_items',
            'created_at',
            'updated_at',
            'total',
            'edited_by',
        ]
        

class TransactionCreateSerializer(serializers.ModelSerializer):
    products = TransactionProductSerializer(many=True , write_only=True)
    transaction_items = TransactionProductSerializer(many=True , read_only=True)
    outlet = OutletSerializer(read_only=True)
    total = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    class Meta:
        model = Transaction
        fields = "__all__"
        extra_kwargs = {
            'transaction_items': {'read_only':True},
            'created_by': {'read_only':True},
            'deleted': {'write_only':True},
            'edited_by': {'read_only':True},
        }

    def create(self, validated_data):
        products = validated_data.pop('products')
        transaction = Transaction.objects.create(**validated_data)
        for product in products:
            print(product)
            # product_id = product['product']
            TransactionProduct.objects.create(transaction=transaction , **product)
        return transaction

    def update(self, instance, validated_data):
        instance.transaction_items.all().delete()  # Clear existing items
        products = validated_data.pop('products')
        for product in products:
            TransactionProduct.objects.create(transaction=instance , **product)
        return super().update(instance, validated_data)
    

