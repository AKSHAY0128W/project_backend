from importlib.resources import contents
from django.shortcuts import render,redirect
from display.models import Services, serviceBooking, Packages, PackageBooking, employee_service_schedule,employee_package_schedule
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
from course.models import course_booking
from django.db.models import Q
from django.db.models import Prefetch
from django.utils import timezone
from django.contrib import messages
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
        booking = serviceBooking(customer=customer, date=date, service=selected_service)
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
        date = datetime.now().date()
        duration = request.POST.get('duration')
        accountants = request.POST.get('accountants')

        # make_payment(request, id)
        booking = PackageBooking(customer=customer, date=date,duration=duration, no_of_accounts=accountants,package=selected_package)
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

        messages.success(request, 'Your appointment has been booked.')
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


def admin_employee_service_schedule(request):
    if request.method == 'POST':
        employee_ids = request.POST.getlist('employee')
        servbooking_id = request.POST.get('booking')
        datetime_str = request.POST.get('datetime')
        datetime = timezone.datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M')
        servbooking = serviceBooking.objects.get(id=servbooking_id)
        for employee_id in employee_ids:
            employee = Employee.objects.get(employee_id=employee_id)
            # Check if the employee is already assigned to a booking on the selected date
            if not employee_service_schedule.objects.filter(employee=employee, datetime__date=datetime.date()).exists():
                employee_service_schedule.objects.create(employee=employee, servbooking=servbooking, datetime=datetime)
            else:
                messages.error(request, f'Employee {employee.name} is already assigned on this date.')
        return redirect('admin_employee_service_schedule')
    else:
        current_date = timezone.now().date()
        scheduled_servbookings = employee_service_schedule.objects.values_list('servbooking', flat=True)
        servbookings = serviceBooking.objects.filter(~Q(id__in=scheduled_servbookings))
        scheduled_employees_service = employee_service_schedule.objects.filter(datetime__date=current_date).values_list('employee', flat=True)
        scheduled_employees_package = employee_package_schedule.objects.filter(datetime__date=current_date).values_list('employee', flat=True)
        employees = Employee.objects.filter(~Q(employee_id__in=scheduled_employees_service) & ~Q(employee_id__in=scheduled_employees_package))

        schedule_list = []
        for booking in serviceBooking.objects.all():
            for schedule in booking.employee_service_schedule_set.all():
                schedule_list.append({
                    'booking': booking,
                    'datetime': schedule.datetime,
                    'employees': [schedule.employee],
                })

        context = {'employees': employees, 'servbookings': servbookings, 'schedule_list': schedule_list}

    return render(request, 'admin_employee_service_schedule.html', context)

def admin_package_schedule(request):
    if request.method == 'POST':
        employee_ids = request.POST.getlist('employee')
        packbooking_id = request.POST.get('booking')
        datetime_str = request.POST.get('datetime')
        datetime = timezone.datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M')
        packbooking = PackageBooking.objects.get(id=packbooking_id)
        for employee_id in employee_ids:
            employee = Employee.objects.get(employee_id=employee_id)
            # Check if the employee is already assigned to a booking on the selected date
            if not employee_package_schedule.objects.filter(employee=employee, datetime__date=datetime.date()).exists():
                employee_package_schedule.objects.create(employee=employee, packbooking=packbooking, datetime=datetime)
            else:
                messages.error(request, f'Employee {employee.name} is already assigned on this date.')
        return redirect('admin_package_schedule')
    else:
        current_date = timezone.now().date()
        scheduled_packbookings = employee_package_schedule.objects.values_list('packbooking', flat=True)
        packbookings = PackageBooking.objects.filter(~Q(id__in=scheduled_packbookings))
        scheduled_employees_package = employee_package_schedule.objects.filter(datetime__date=current_date).values_list('employee', flat=True)
        scheduled_employees_service = employee_service_schedule.objects.filter(datetime__date=current_date).values_list('employee', flat=True)
        employees = Employee.objects.filter(~Q(employee_id__in=scheduled_employees_package) & ~Q(employee_id__in=scheduled_employees_service))

        schedule_list = []
        for booking in PackageBooking.objects.all():
            for schedule in booking.employee_package_schedule_set.all():
                schedule_list.append({
                    'booking': booking,
                    'datetime': schedule.datetime,
                    'employees': [schedule.employee],
                })

        context = {'employees': employees, 'packbookings': packbookings, 'schedule_list': schedule_list}

    return render(request, 'admin_employee_package_schedule.html', context)

def admin_course_booking_details(request):
    courseBooking = course_booking.objects.all()
    return render(request, 'admin_course_booking_details.html', {'courseBooking': courseBooking})

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

@login_required
def customer_my_appointments(request):
    profile = Profile.objects.get(user=request.user)
    customer = Customer.objects.get(profile=profile)
    appointments = Appointment.objects.filter(name=customer.name, email=customer.email)

    return render(request, 'customer_my_appointments.html', {'appointments': appointments})



@login_required
def employee_my_schedule(request):
    # Get the Profile object for the logged-in user
    profile = Profile.objects.get(user=request.user)

    # Get the Employee object for the profile
    employee = Employee.objects.get(profile=profile)

    # Get the schedule for the employee
    my_schedule = employee_service_schedule.objects.filter(employee=employee)

    return render(request, 'employee_my_schedule.html', {'my_schedule': my_schedule})