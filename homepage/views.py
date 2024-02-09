from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from display.models import Services
from login_registration.models import Customer, Employee
from django.contrib.sessions.models import Session
from django.utils import timezone

def default(request):
    services = Services.objects.all()
    context = {'services':services}
    return render(request, 'default.html', context)
    
def homepage(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def appointment(request):
    return render(request, 'appointment.html')

def dashboard(request):
    return render(request, 'customer.html')

def myservices(request):
    services = Services.objects.all()
    context = {'services':services}
    print(services)
    return render(request, 'services.html', context)

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def employee_panel(request):
    return render(request, 'employee.html')

def services(request):
    return render(request, 'services.html')

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