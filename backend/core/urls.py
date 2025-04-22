"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

# views
from brand.views import BrandView , BrandDetailView
from product.views import ProductListCreateView , ProductRetrieveUpdateDestroyView
from transaction.views import TransactionListCreateView,TransactionRetrieveUpdateDestroyView
from outlet.views import OutletListCreateView , OutletRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/brands/', BrandView.as_view()),
    path('api/brand/<int:pk>/' ,BrandDetailView.as_view()),
    path('api/products/' , ProductListCreateView.as_view()),
    path('api/product/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view()),
    path('api/transactions/', TransactionListCreateView.as_view()),
    path('api/transaction/<int:pk>/', TransactionRetrieveUpdateDestroyView.as_view()),
    path('api/outlets/', OutletListCreateView.as_view()),
    path('api/outlet/<int:pk>/', OutletRetrieveUpdateDestroyView.as_view()),
]
