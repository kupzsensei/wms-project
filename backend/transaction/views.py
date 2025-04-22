from django.shortcuts import render
from rest_framework import generics
from .models import Transaction , TransactionProduct
from .serializers import  TransactionListSerializer , TransactionCreateSerializer
from django.db.models import Sum , F , ExpressionWrapper , DecimalField
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.filter(deleted=False).order_by('-id').annotate(total=Sum(
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
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.filter(deleted=False).prefetch_related('products').select_related('created_by','outlet','edited_by').order_by('-id').annotate(total=Sum(
        ExpressionWrapper(
            F('transaction_items__price') * F('transaction_items__quantity'),
            output_field=DecimalField(max_digits=12, decimal_places=2)
        )
    ))
    serializer_class = TransactionCreateSerializer

    def update(self, request, *args, **kwargs):
        request.data['edited_by'] = request.user.id
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted = True
        instance.save()
        return Response({"detail": "Transaction successfully deleted."}, status=status.HTTP_204_NO_CONTENT)