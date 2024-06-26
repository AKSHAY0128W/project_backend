from appointment.models import *
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import PackageBooking, Services, Packages
from .models import serviceBooking
from login_registration.models import *
from django.shortcuts import render, redirect
from display.models import payment
from django.contrib.auth.decorators import login_required
# employee

def emp_display(request):
    emp = Employee.objects.all()
    des = Designation.objects.all()
    # print(emp)
    context = {
        'des':des,
        'emp':emp,
    }
    return render(request, 'admin_employee_details.html', context)

def emp_edit(request,employee_id):
    emp = Employee.objects.get(employee_id=employee_id)
    context = {
        'emp':emp,  
        
    }
    return render(request, 'admin_employee_details.html', context)

def emp_update(request, employee_id):
    emp = Employee.objects.get(employee_id=employee_id)  
        
    if request.method == "POST":
            emp.name = request.POST.get('name')
            emp.email = request.POST.get('email')
            emp.phone = request.POST.get('phone')
            emp.address = request.POST.get('address')
            designation_id = request.POST.get('designation')
            emp.designation = Designation.objects.get(id=designation_id)
            emp.save() 
            return redirect('/emp_display')
        
    context = {
        'emp': emp,
    }
    return render(request, 'admin_employee_details.html', context)


def emp_delete(request, employee_id):
    emp = Employee.objects.filter(employee_id=employee_id)
    emp.delete()
    context = {
        'emp':emp,
    }
    return redirect('/emp_display', context)


# services
def services_list(request):
    services = Services.objects.all()
    # print(services)
    context = {
        'services':services,
    }

    return render(request, 'admin_service_details.html', context)

def add_service(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        price = request.POST.get('price')

        if not price:
            price = 0 

        Services.objects.create(name=name, description=description, image=image, price=price)

        return redirect('/services_list')

    return render(request, 'admin_service_details.html')



def services_edit(request, id):
    services = Services.objects.get(id=id)
    context = {
        'services':services,
    }
    return render(request, 'admin_service_details.html', context)


def services_update(request, id):
    services = Services.objects.get(id=id)  
    if request.method == "POST":
        services.name = request.POST.get('name')
        services.description = request.POST.get('description')
        services.price = request.POST.get('price')

        if 'image' in request.FILES:
            services.image = request.FILES['image']

        services.save()  
        return redirect('/services_list')
    return render(request, 'admin_service_details', {'services': services})


def services_delete(request, id):
    services = Services.objects.filter(id=id)
    services.delete()
    context = {
        'services':services,
    }
    return redirect('/services_list', context)


#appointment
def admin_appointment_list(request):
    admin_appointment_list = Appointment.objects.all()
    context = {
        'admin_appointment_list':admin_appointment_list,
    }
    return render(request, 'admin_appointment_details.html', context)

#serviceBooking

def service_booking_admin(request):
    bookings = serviceBooking.objects.select_related('customer').all()
    return render(request, 'admin_service_booking_details.html', {'bookings': bookings})


def booking_delete(request, id):
    booking = serviceBooking.objects.filter(id=id)
    booking.delete()
    return redirect('/service_booking_admin')


def package_booking_admin(request):
    bookings = PackageBooking.objects.select_related('customer').all()
    return render(request, 'admin_package_booking_details.html', {'bookings': bookings})

#payments

def payment_list(request):
    payments = payment.objects.all()
    # print(payments)
    context = {
        'payments':payments,
    }
    return render(request, 'admin_payments_details.html', context)


# packages
def add_packages(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')

        if not price:
            price = 0  

        Packages.objects.create(name=name, description=description,price=price)

        return redirect('/packages_list')

    return render(request, 'admin_package_details.html')

def packages_list(request):
    packages = Packages.objects.all()
    # print(packages)
    context = {
        'packages':packages,
    }
    return render(request, 'admin_package_details.html', context)

def packages_edit(request, id):
    packages = Packages.objects.get(id=id)
    context = {
        'packages':packages,
    }
    return render(request, 'admin_package_details.html', context)

def packages_update(request, id):
    packages = Packages.objects.get(id=id)  
    if request.method == "POST":
        packages.name = request.POST.get('name')
        packages.description = request.POST.get('description')
        packages.price = request.POST.get('price')
        packages.duration = request.POST.get('duration')

        packages.save()
        return redirect('/packages_list')

    return render(request, 'admin_package_details', {'packages': packages})

def packages_delete(request, id):
    packages = Packages.objects.filter(id=id)
    packages.delete()
    context = {
        'packages':packages,
    }
    return redirect('/packages_list', context)


#customers
def customer_list(request):
    customer = Customer.objects.all()
    # print(customer)
    context = {
        'customer':customer,
    }
    return render(request, 'admin_customer_details.html', context)

def customer_delete(request, id):
    customer = Customer.objects.filter(id=id)
    customer.delete()
    context = {
        'customer':customer,
    }
    return redirect('/customer_list', context)

#employee

def employee_customer_list(request):
    customer_list = Customer.objects.all()
    context = {
        'customer_list':customer_list,
    }
    return render(request, 'employee_customer_details.html', context)

def employee_appointment_list(request):
    appointment_list = Appointment.objects.all()
    context = {
        'appointment_list':appointment_list,
    }
    return render(request, 'employee_appointment_details.html', context)

def employee_service_booking_list(request):
    bookings = serviceBooking.objects.select_related('customer').all()
    return render(request, 'employee_service_booking_details.html', {'bookings': bookings})



def employee_payment_list(request):
    payments = payment.objects.all()
    # print(payments)
    context = {
        'payments':payments,
    }
    return render(request, 'employee_payments_details.html', context)


def employee_package_booking_list(request):
    bookings = PackageBooking.objects.select_related('customer').all()
    return render(request, 'employee_package_booking_list.html', {'bookings': bookings})