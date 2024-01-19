from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


def default(request):
    return render(request, 'default.html')
    
@login_required(login_url='login')
def homepage(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def aboutus(request):
    return render(request, 'aboutus.html')

@login_required(login_url='login')
def appointment(request):
    return render(request, 'appointment.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'customer.html')

@login_required(login_url='login')
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required(login_url='login')
def employee_panel(request):
    return render(request, 'employee.html')

@login_required(login_url='login')
def services(request):
    return render(request, 'services.html')

@login_required(login_url='login')
def admin_login(request):
    # if user is super user he will redirect to admin dashboard
    if request.user.is_superuser:
        return redirect(request, 'admin_dashboard')
    else:
        return render(request, 'admin_login')
    return render(request, 'login.html')

@login_required(login_url='login')
def admin_create_employee(request):
    return render(request, 'admin_create_employee.html')

@login_required(login_url='login')
def admin_homepage(request):
    return render(request, 'admin_dashboard.html')

@login_required(login_url='login')
def admin_view_employee(request):
    return render(request, 'admin_employee_details.html')

@login_required(login_url='login')
def admin_service_details(request):
    return render(request, 'admin_service_details.html')