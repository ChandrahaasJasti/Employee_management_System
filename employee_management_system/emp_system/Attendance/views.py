from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee,Department
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def test_hi(request):
    return HttpResponse("Hello World")


@csrf_exempt
def add_employee(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        dept_id = data.get('dept')
        dept_instance = None
        if dept_id is not None:
            try:
                dept_instance = Department.objects.get(id=dept_id)
            except Department.DoesNotExist:
                return HttpResponse("Department not found", status=400)
        emp = Employee(name=name, email=email, dept=dept_instance)
        emp.save()
        return HttpResponse("Employee added successfully")
    return render(request, 'add_employee.html')

@csrf_exempt
def add_dept(request):
    if request.method=="POST":
        data=json.loads(request.body)
        name=data.get('name')
        dept=Department(name=name)
        dept.save()
        return HttpResponse("Department added successfully")
    return render(request, 'add_dept.html')