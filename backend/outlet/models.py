from django.db import models

# Create your models here.
class Outlet(models.Model):
    name = models.CharField(max_length=255 , unique=True)
    address = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=20 , blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name