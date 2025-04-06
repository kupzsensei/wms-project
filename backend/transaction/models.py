from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from django.core.validators import MinValueValidator
from decimal import Decimal

# Create your models here.
class TransactionProduct(models.Model):
    product = models.ForeignKey(Product , on_delete=models.PROTECT )
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE , related_name='transaction_items')
    price = models.DecimalField(max_digits=100 , decimal_places=2 , validators=[MinValueValidator(Decimal('1.00'))])
    quantity = models.IntegerField()

    @property
    def subtotal(self):
        return self.price * self.quantity



class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        DELIVERY = 'delivery' , 'Delivery'
        RECEIVE = 'receive' , 'Receive'
        TRANSFER = 'transfer' , 'Transfer'
    # created_by = models.ForeignKey(User , on_delete=models.CASCADE)
    transaction_number = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=50 , choices=TransactionType.choices , default=TransactionType.DELIVERY)
    edited_by = models.ForeignKey(User , on_delete=models.PROTECT)
    #timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # related fields
    # products

    