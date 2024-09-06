from django.db import models

class Employee(models.Model):
    empid=models.IntegerField()
    empname=models.CharField(max_length=20)
    empsalary=models.IntegerField()
    empaddress=models.CharField(max_length=100)
    def __str__(self):
        return str(self.empid)+" "+self.empname+" "+str(self.empsalary)+" "+self.empaddress

class Student(models.Model):
    rollno=models.IntegerField(default=0,primary_key=True)
    name=models.CharField(max_length=30)
