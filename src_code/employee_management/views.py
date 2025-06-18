from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import *
from .forms import *
# Create your views here.

def employees(request):
    employees = Employee.objects.all()[:10]
    emp_count = Employee.objects.count() > 10
    context = {
        'employees': employees ,
        'emp_count' : emp_count
    }
    return render(request, 'employee_management/employee.html' , context)

def add_employee(request):
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee:emp_index')  # Redirect to a success page or list view.
    else:
        form = AddEmployeeForm()
    
    return render(request, 'employee_management/add_employee.html', {'form': form})

def update_employee(request, pk):
    employee = Employee.objects.get(id = pk)
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee:employees_alter')  # Redirect to a success page or list view.
    else:
        form = AddEmployeeForm(instance=employee)
    return render(request, 'employee_management/update_employee.html', {'form': form})

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, id=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('employee:employees_alter')  

    # Render a confirmation page for GET requests
    return render(request, 'employee_management/delete_employee.html', {'employee': employee})


def all_employees(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees ,
    }
    return render(request, 'employee_management/all_employee.html' , context)

def employees_alter(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees ,
    }
    return render(request, 'employee_management/employees_alter.html' , context)
