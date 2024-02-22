from django.shortcuts import render,redirect
from display.models import Services, serviceBooking, Packages
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

def make_payment(request, id): 
    selected_service = get_object_or_404(Services, id=id)

    profile = get_object_or_404(Profile, user=request.user)
    customer = profile.customer  

    if not Customer.objects.filter(id=customer.id).exists():  
        return HttpResponse('Customer does not exist', status=400)
    
    if request.method == 'POST':

        date = datetime.now().date()
        time = datetime.now().time()

        print(date, time, customer, selected_service)
        payment_instance = payment(date=date, time=time, customer=customer, service=selected_service)
        payment_instance.save()

        return redirect('myservices')
        
    return render(request, 'payment.html', {'service_name': selected_service.name, 'service_price': selected_service.price, 'customer': customer, 'service_id': id})


def default(request):
    services = Services.objects.all()
    context = {'services':services}
    return render(request, 'default.html', context)
    
def homepage(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')


@login_required
def appointment(request):
    if request.method == 'POST':
        # Get name and email from the Customer table
        customer = Customer.objects.get(user=request.user)
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

def myservices(request):
    services = Services.objects.all()
    context = {'services':services}
    print(services)
    return render(request, 'services.html', context)

def mypackages(request):

    packages = Packages.objects.all()
    context = {'packages':packages}
    print(packages)
    return render(request, 'packages.html', context)



def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def employee_panel(request):
    return render(request, 'employee.html')

def services(request):
    return render(request, 'services.html')


@login_required
def service_booking(request, id):
    # Get the selected service
    selected_service = get_object_or_404(Services, id=id)

    # Try to get the profile for the currently logged-in user
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # Handle the case where the profile does not exist
        # For example, you can return an HTTP 404 response
        return HttpResponse('Profile does not exist', status=404)

    # Get the customer related to this profile
    customer = profile.customer  # replace 'customer' with the actual related name

    # Check if the customer exists
    if not Customer.objects.filter(id=customer.id).exists():
        return HttpResponse('Customer does not exist', status=400)

    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')

        # Create a new serviceBooking instance with the customer and selected service
        booking = serviceBooking(customer=customer, date=date, time=time, service=selected_service)
        booking.save()

        # Redirect to the payment page for the selected service
        return redirect(reverse('make_payment', args=[selected_service.id]))

    return render(request, 'service_booking.html', {'selected_service': selected_service})





def admin_login(request):

    # if user is super user he will redirect to admin dashboard
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
    context = {'user_count': user_count, 'logged_in_user_count': logged_in_user_count, 'totalemployee': totalemployee}
    return render(request, 'admin_homepage.html', context)

def admin_view_employee(request):
    return render(request, 'admin_employee_details.html')

def admin_service_details(request):
    return render(request, 'admin_service_details.html')