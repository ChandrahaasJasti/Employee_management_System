from django.urls import path
from . import views

urlpatterns = [
    path('test/hi/', views.test_hi, name='hi'),
]