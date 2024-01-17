from django.shortcuts import render

# Create your views here.
from login_registration.models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect

def emp_display(request):
    emp = Employee.objects.all()
    print(emp)
    context = {
        'emp':emp,
    }
    return render(request, 'admin_employee_details.html', context)

def emp_edit(request, id):
    emp = Employee.objects.get(id=id)
    context = {
        'emp':emp,
    }
    return render(request, 'admin_edit_employee.html', context)

def emp_update(request,id):
    if request.method == "POST":
        emp = Employee.objects.get(id = id)  # fetch the Employee object
        emp.name = request.POST.get('name')
        emp.email = request.POST.get('email')
        emp.phone = request.POST.get('phone')
        emp.address = request.POST.get('address')
        emp.save()  # save the updated Employee object
        return redirect('/emp_display')
    
    return render(request, 'admin_edit_employee.html')
