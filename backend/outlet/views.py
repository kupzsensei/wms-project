from django.shortcuts import render
from .models import Outlet
from .serializers import OutletSerializer
from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import DjangoModelPermissions

# Create your views here.
class OutletListCreateView(generics.ListCreateAPIView):
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name" , "address"]
    permission_classes = [DjangoModelPermissions]


class OutletRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Outlet.objects.all()
    serializer_class = OutletSerializer
    permission_classes = [DjangoModelPermissions]
