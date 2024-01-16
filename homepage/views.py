from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def homepage(request):
    return render(request, 'index.html')

def default(request):
    return render(request, 'default.html')

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
    return render(request, 'latest_admin.html')

@login_required(login_url='login')
def services(request):
    return render(request, 'services.html')

def admin_login(request):
    # if user is super user he will redirect to admin dashboard
    if request.user.is_superuser:
        return redirect(request, 'latest_admin.html')
    else:
        return render(request, 'admin_login.html')
    return render(request, 'login.html')