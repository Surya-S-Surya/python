from django.db import models

class Employee(models.Model):
    empid=models.IntegerField()
    empname=models.CharField(max_length=20)
    empsalary=models.IntegerField()
    empaddress=models.CharField(max_length=60)
