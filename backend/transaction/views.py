from django.shortcuts import render
from rest_framework import generics
from .models import Transaction , TransactionProduct
from .serializers import  TransactionListSerializer , TransactionCreateSerializer
from django.db.models import Sum , F , ExpressionWrapper , DecimalField

# Create your views here.
class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all().order_by('-id').annotate(total=Sum(
        ExpressionWrapper(
            F('transaction_items__price') * F('transaction_items__quantity'),
            output_field=DecimalField(max_digits=12, decimal_places=2)
        )
    ))
    serializer_class = TransactionCreateSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TransactionListSerializer
        return super().get_serializer_class()