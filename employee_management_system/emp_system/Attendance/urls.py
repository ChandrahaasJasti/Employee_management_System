from django.urls import path
from . import views

urlpatterns = [
    path('test/hi/', views.test_hi, name='hi'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('add_dept/', views.add_dept, name='add_dept')
]