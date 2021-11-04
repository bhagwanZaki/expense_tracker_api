from django.shortcuts import render
from api.models import expense, totalAmount
from rest_framework import permissions,status
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date as dt
import calendar

class DashboardAPi(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self,request,format=None):
        expenseData = expense.objects.filter(user_linked=request.user)
        try:
            totalAmt = totalAmount.objects.filter(user_linked=request.user)[0].amount

            pass
        except:
            totalAmt = 0.0
            pass
        total_amount = 0
        incomeAmt = 0
        savingAmt = 0
        expenseAmt = 0

        CurrentMonthData= expenseData.filter(amount_date__year=dt.today().year,amount_date__month=dt.today().month)
        for i in CurrentMonthData:
            if i.incomeOrexpense == 'income':
                incomeAmt+=i.amount
            elif i.incomeOrexpense == 'saving':
                savingAmt+=i.amount
            else:
                expenseAmt+=i.amount

        totalAmt += (savingAmt + incomeAmt) - expenseAmt
        currentYear = dt.today().year
        currentMonth = dt.today().month
        if expenseData:

            data = expenseData.order_by('amount_date')[0]
            startYear = data.amount_date.year
            startMonth = data.amount_date.month

            
            if startYear != currentYear:
                dayList = [i for i in range(1, calendar.monthrange(dt.today().year, dt.today().month)[1]+1)]
            else:
                if startMonth != currentMonth:
                    startDay = 1
                else:
                    startDay = data.amount_date.day
                
                dayList = [i for i in range(startDay,calendar.monthrange(dt.today().year, dt.today().month)[1]+1)]

            income_graph_data = []
            expense_graph_data = []
            saving_graph_data = []

            for i in range(startDay,dt.today().day+1):
                current_day_expense = expenseData.filter(amount_date__year=dt.today().year,amount_date__month=dt.today().month,amount_date__day=i)
                income_graph_data.append(current_day_expense.filter(incomeOrexpense='income').count())
                expense_graph_data.append(current_day_expense.filter(incomeOrexpense='expense').count())
                saving_graph_data.append(current_day_expense.filter(incomeOrexpense='saving').count())
        else:
            dayList = [i for i in range(1, calendar.monthrange(dt.today().year, dt.today().month)[1]+1)]
            income_graph_data = []
            expense_graph_data = []
            saving_graph_data = []

            pass
        
        context = {
            "total_amount":totalAmt,
            "incomeAmt":incomeAmt,
            "savingAmt":savingAmt,
            "expenseAmt":expenseAmt,

            "dayList":dayList,
            
            "income_graph_data":income_graph_data,
            "saving_graph_data":saving_graph_data,
            "expense_graph_data":expense_graph_data,

            "total_income_count":sum(income_graph_data),
            "total_saving_count":sum(saving_graph_data),
            "total_expense_count":sum(expense_graph_data)
        }

        return Response(context,status=status.HTTP_200_OK)