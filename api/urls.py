from .views import *
from rest_framework import routers
from django.urls import path

router = routers.DefaultRouter()
router.register('api/expense',ExpenseViewSet,'expenses')

urlpatterns =[]

urlpatterns += router.urls