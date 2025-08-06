from django.db import models

# Create your models here.
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)



# class attendance(models.Model):
#     id=models.AutoField(primary_key=True),
#     emp_id=models.ForeignKey(Employee, on_delete=models.CASCADE),
#     date=models.DateField(),
#     status=models.CharField(max_length=100)