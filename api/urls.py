from .views import *
from rest_framework import routers
from django.urls import path

router = routers.DefaultRouter()
router.register('api/expense',ExpenseViewSet,'expenses')
router.register('api/test',kotlinTestViewSet,'testexpenses')

urlpatterns =[]

urlpatterns += router.urls