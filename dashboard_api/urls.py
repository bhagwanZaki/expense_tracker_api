from django.urls import path
from .views import *

urlpatterns = [
    path('api/dashboard/',DashboardAPi.as_view()),
]