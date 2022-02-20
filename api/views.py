from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework import permissions,status,serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date as dt
import calendar
from .models import *

class ExpenseViewSet(ModelViewSet):
    serializer_class = expenseSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return self.request.user.expense.all()

    def perform_create(self, serializer):
        amt = serializer.validated_data.get('amount')
        transcType = serializer.validated_data.get('incomeOrexpense')
        totalAmountdata = totalAmount.objects.filter(user_linked=self.request.user).get()
        totalAmt = totalAmountdata.amount
        if transcType == 'expense':
            totalAmt -= amt
        else:
            totalAmt += amt
        if totalAmt >= 0:
            serializer.save(user_linked=self.request.user)
            totalAmountdata.amount = totalAmt
            totalAmountdata.save()
        else:
            print('fail')
            raise serializers.ValidationError('Expense cannot be greater than total amount')