from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test_hi(request):
    return HttpResponse("Hello World")

def add_employee(request):
    