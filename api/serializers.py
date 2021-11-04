from rest_framework import serializers
from .models import *

class expenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = expense
        fields = '__all__'