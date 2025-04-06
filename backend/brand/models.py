from django.db import models

# Create your models here.
class Brand(models.Model):
    # required fields
    name = models.CharField(max_length=200)
    # Optional Fields
    description = models.TextField(null=True , blank=True)
    # timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
