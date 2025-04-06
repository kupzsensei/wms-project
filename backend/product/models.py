from django.db import models
from brand.models import Brand

# Create your models here.
class Product(models.Model):
    code = models.CharField(max_length=50 , unique=True)
    sku = models.CharField(max_length=100 , unique=True , null=True)
    barcode = models.CharField(max_length=100 , unique=True , null=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    brand = models.ForeignKey(Brand , on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=100 , decimal_places=2)

    # timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} - {self.name} ({self.description}) P{self.price}"