from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.IntegerField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
