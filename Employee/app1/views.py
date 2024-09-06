from django.shortcuts import render, get_object_or_404
from .models import Employee
from .forms import EmployeeForm, SearchForm

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, you can add a success message or redirect to another page
            return render(request, 'employee_added.html')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

def search_employee(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee_id']
            employee = Employee.objects.get(employee_id=employee_id)
            return render(request, 'employee_details.html', {'employee': employee})
    else:
        form = SearchForm()
    return render(request, 'search_employee.html', {'form': form})
