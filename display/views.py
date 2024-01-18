from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
# Create your views here.
from .models import *
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
    return render(request, 'admin_employee_details.html', context)



def emp_update(request, employee_id):
    emp = get_object_or_404(Employee, employee_id=employee_id)  # fetch the Employee object or return 404 if not found

    if request.method == "POST":
        emp.name = request.POST.get('name')
        emp.email = request.POST.get('email')
        emp.phone = request.POST.get('phone')
        emp.address = request.POST.get('address')
        emp.save()  # save the updated Employee object
        return redirect('/emp_display')

    return render(request, 'admin_employee_details', {'emp': emp})

def emp_delete(request, employee_id):
    emp = Employee.objects.filter(employee_id=employee_id)
    emp.delete()
    context = {
        'emp':emp,
    }
    return redirect('/emp_display', context)



def add_service(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        Services.objects.create(name=name, description=description, image=image)

        return redirect('/services_list')

    return render(request, 'admin_service_details.html')

def services_list(request):
    services = Services.objects.all()
    print(services)
    context = {
        'services':services,
    }
    return render(request, 'admin_service_details.html', context)

def services_edit(request, id):
    services = Services.objects.get(id=id)
    context = {
        'services':services,
    }
    return render(request, 'admin_service_details.html', context)


from django.core.files import File

def services_update(request, id):
    services = Services.objects.get(id=id)  # fetch the Services object or return 404 if not found
    if request.method == "POST":
        services.name = request.POST.get('name')
        services.description = request.POST.get('description')

        # handle file upload
        if 'image' in request.FILES:
            services.image = request.FILES['image']

        services.save()  # save the updated Services object
        return redirect('/services_list')

    return render(request, 'admin_service_details', {'services': services})

def services_delete(request, id):
    services = Services.objects.filter(id=id)
    services.delete()
    context = {
        'services':services,
    }
    return redirect('/services_list', context)
