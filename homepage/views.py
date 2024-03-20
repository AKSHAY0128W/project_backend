from django.shortcuts import render,redirect
from display.models import Services, serviceBooking, Packages, PackageBooking, employee_service_schedule
from login_registration.models import Customer, Employee, Profile
from django.contrib.sessions.models import Session
from appointment.models import Appointment
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from display.models import payment

# def make_payment(request, id): 
#     selected_service = get_object_or_404(Services, id=id)

#     profile = get_object_or_404(Profile, user=request.user)
#     customer = profile.customer  

#     if not Customer.objects.filter(id=customer.id).exists():  
#         return HttpResponse('Customer does not exist', status=400)
    
#     if request.method == 'POST':

#         date = datetime.now().date()
#         time = datetime.now().time()

#         booking = serviceBooking(customer=customer, date=date, time=time, service=selected_service)
#         booking.save()

#         # Create a new payment instance with the customer and selected service
#         payment_instance = payment(date=date, time=time, customer=customer, service=selected_service)
#         payment_instance.save()

#         return redirect('myservices')
        
#     return render(request, 'payment.html', {'service_name': selected_service.name, 'service_price': selected_service.price, 'customer': customer, 'service_id': id})

@login_required
def service_booking(request, id):
    selected_service = get_object_or_404(Services, id=id)

    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return HttpResponse('Profile does not exist', status=404)

    customer = profile.customer  # replace 'customer' with the actual related name

    if not Customer.objects.filter(id=customer.id).exists():
        return HttpResponse('Customer does not exist', status=400)

    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')

        # make_payment(request, id)
        booking = serviceBooking(customer=customer, date=date, time=time, service=selected_service)
        booking.save()
        
        return redirect('myservices')

    return render(request, 'service_booking.html', {'selected_service': selected_service})

    
    

def package_booking(request, id):
    selected_package = get_object_or_404(Packages, id=id)

    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return HttpResponse('Profile does not exist', status=404)

    customer = profile.customer  # replace 'customer' with the actual related name

    if not Customer.objects.filter(id=customer.id).exists():
        return HttpResponse('Customer does not exist', status=400)

    if request.method == 'POST':
        comapany_name = request.POST.get('cname')
        company_address = request.POST.get('cadd')
        date = request.POST.get('date')

        # make_payment(request, id)
        booking = PackageBooking(customer=customer, date=date, company_name=comapany_name, company_address=company_address, package=selected_package)
        booking.save()
        
        return redirect('packages')

    return render(request, 'package_booking.html', {'selected_package': selected_package})


def default(request):
    services = Services.objects.all()
    packages = Packages.objects.all()
    context = {'services':services, 'packages':packages}
    return render(request, 'default.html', context)
    
def homepage(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')


@login_required
def appointment(request):
    if request.method == 'POST':
        # Get name and email from the Customer table
        profile = Profile.objects.get(user=request.user)
        customer = Customer.objects.get(profile=profile)
        name = customer.name
        email = customer.email

        date = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')        
        print(name, email, date, time, message)

        appointment = Appointment(name=name, email=email, date=date, time=time, message=message)
        appointment.save()

        return render(request, 'appointment.html')
    return render(request, 'appointment.html')

def dashboard(request):
    return render(request, 'customer.html')

@login_required
def myservices(request):
    profile = get_object_or_404(Profile, user=request.user)
    customer = profile.customer
    booked_services_ids = serviceBooking.objects.filter(customer=customer).values_list('service__id', flat=True)
    services = Services.objects.exclude(id__in=booked_services_ids)
    return render(request, 'services.html', {'services': services})

def mypackages(request):
    profile = get_object_or_404(Profile, user=request.user)
    customer = profile.customer
    booked_packages_ids = PackageBooking.objects.filter(customer=customer).values_list('package__id', flat=True)
    packages = Packages.objects.exclude(id__in=booked_packages_ids)
    return render(request, 'packages.html', {'packages': packages})



def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def employee_panel(request):
    return render(request, 'employee.html')

def services(request):
    return render(request, 'services.html')



def admin_login(request):

    if request.user.is_superuser:
        return redirect(request, 'admin_dashboard')
    else:
        return render(request, 'admin_login')
    return render(request, 'login.html')

def admin_create_employee(request):
    return render(request, 'admin_create_employee.html')

def admin_homepage(request):
    user_count = Customer.objects.count()
    logged_in_user_count = Session.objects.filter(expire_date__gte=timezone.now()).count()
    totalemployee = Employee.objects.count()
    totalservice_booking = serviceBooking.objects.count()
    totalpayments = payment.objects.count()
    context = {'user_count': user_count, 'logged_in_user_count': logged_in_user_count, 'totalemployee': totalemployee, 'totalservice_booking': totalservice_booking, 'totalpayments': totalpayments}
    return render(request, 'admin_homepage.html', context)

def admin_view_employee(request):
    return render(request, 'admin_employee_details.html')

def admin_service_details(request):
    return render(request, 'admin_service_details.html')

def admin_employee_schedule(request):
    
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        servbooking_id = request.POST.get('booking')  # Changed booking_id to servbooking_id
        datetime_str = request.POST.get('datetime')
        datetime = timezone.datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M')
        employee = Employee.objects.get(employee_id=employee_id)
        servbooking = serviceBooking.objects.get(id=servbooking_id)  # Changed booking to servbooking
        employee_service_schedule.objects.create(employee=employee, servbooking=servbooking, datetime=datetime)  # Changed booking to servbooking
        return redirect('admin_employee_schedule')
    else:
        employees = Employee.objects.all()
        servbookings = serviceBooking.objects.all()  # Changed bookings to servbookings
        context = {'employees': employees, 'servbookings': servbookings}  # Changed bookings to servbookings


        return render(request, 'admin_employee_schedule.html', context)
        
@login_required
def customer_my_services(request):
    profile = get_object_or_404(Profile, user=request.user)
    customer = profile.customer
    booked_services = serviceBooking.objects.filter(customer=customer)
    return render(request, 'customer_my_services.html', {'booked_services': booked_services})


@login_required
def customer_my_packages(request):
    profile = get_object_or_404(Profile, user=request.user)
    customer = profile.customer
    booked_packages = PackageBooking.objects.filter(customer=customer)
    return render(request, 'customer_my_packages.html', {'booked_packages': booked_packages})


def customer_my_coures(request):
    return render(request, 'customer_my_courses.html')