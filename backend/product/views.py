from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductCreateSerializer , ProductListSerializer

# Create your views here.
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.select_related('brand')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductListSerializer
        return ProductCreateSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer