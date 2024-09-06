from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'employee_id', 'salary', 'department', 'phone_number']

class SearchForm(forms.Form):
    employee_id = forms.IntegerField()
