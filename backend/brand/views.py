from django.shortcuts import render
from rest_framework import generics
from .serializers import BrandSerializer
from .models import Brand
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.exceptions import APIException
from django.db.models.deletion import ProtectedError
from rest_framework.response import Response
from rest_framework import status 

# Create your views here.
class BrandView(generics.ListCreateAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    permission_classes = [DjangoModelPermissions]

class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except ProtectedError as e:
            # Custom message for ProtectedError
            return Response({
                'detail': f"Cannot delete this brand because it is referenced by other products: {e}. Please remove the references before deleting."
            }, status=status.HTTP_400_BAD_REQUEST)