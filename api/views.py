from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework import permissions,status,serializers
from rest_framework.response import Response
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

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            totalAmountdata = totalAmount.objects.filter(user_linked=request.user).get()
            if instance.incomeOrexpense == 'expense':
                totalAmountdata.amount += instance.amount
            else:
                totalAmountdata.amount -= instance.amount
            totalAmountdata.save()
            print(instance)
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print("do")
            raise serializers.ValidationError(e)