from django.db import models
from django.contrib.auth.models import User

class expense(models.Model):
    CHOICES = [
        ('income','Income'),
        ('expense','Expense'),
        ('saving','Saving'),
    ]
    
    user_linked = models.ForeignKey(User, on_delete=models.CASCADE,related_name='expense',null=True)
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    incomeOrexpense = models.CharField(max_length=7,choices=CHOICES)
    amount_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.user_linked} tracker - {self.pk}'

class totalAmount(models.Model):
    user_linked = models.OneToOneField(User,on_delete=models.CASCADE,related_name='initial',null=True)
    amount = models.FloatField()

    def __str__(self) -> str:
        return f'{self.user_linked} total amount'


class testExpenseTracker(models.Model):
    CHOICES = [
        ('income','Income'),
        ('expense','Expense'),
        ('saving','Saving'),
    ]    
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    incomeOrexpense = models.CharField(max_length=7,choices=CHOICES)
    amount_date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title} record'