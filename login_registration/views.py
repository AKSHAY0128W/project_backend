from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import Customer, Employee, Profile, Designation

from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'indexregister.html')

        if Customer.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'indexregister.html')

        if password1 != password2:
            pass

        try:
            validate_password(password1)
        except ValidationError as e:
            pass

        user = User.objects.create_user(username=username, password=password1)
        user.save()

        profile = Profile(user=user, user_type='customer')
        profile.save()

        customer = Customer(profile=profile,email=email)
        customer.save()

        messages.success(request, 'User created successfully')  

        return redirect ('login')

    return render(request, 'indexregister.html')

    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_homepage')
            elif user.is_staff:
                return redirect('employee_panel')
            else:
                return redirect('homepage')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'indexlogin.html')
    return render(request, 'indexlogin.html')


def logout_view(request):
    logout(request)
    return redirect('default')

def create_employee(request):
    if request.user.is_superuser:
        pos = Designation.objects.all()
        if request.method == 'POST':
            username = request.POST.get('name')
            password = request.POST.get('password')
            email = request.POST.get('email')
            fullname = request.POST.get('fullname')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            designation = request.POST.get('designation')

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return render(request, 'admin_create_employee.html', {'pos': pos})

            if Employee.objects.filter(email=email).exists():
                messages.error(request, 'Email already in use.')
                return render(request, 'admin_create_employee.html', {'pos': pos})

            user = User(username=username, password=make_password(password), is_staff=True)
            user.save()

            profile = Profile(user=user, user_type='employee')
            profile.save()

            employee = Employee(profile=profile, name=fullname,email=email ,phone=phone, address=address, designation_id=designation)
            employee.save()

            return redirect('emp_display')
        else:
            return render(request, 'admin_create_employee.html', {'pos': pos})
    else:
        return redirect('homepage')
    
def customer_my_profile(request):
    if request.user.is_authenticated:
        if request.user.profile.user_type == 'customer':
            customer = Customer.objects.get(profile=request.user.profile)
            if request.method == 'POST':
                customer.name = request.POST.get('name')
                customer.email = request.POST.get('email')
                customer.address = request.POST.get('address')
                customer.phone = request.POST.get('phone')
                customer.company_name = request.POST.get('company_name')
                customer.company_address = request.POST.get('company_address')
                customer.company_phone = request.POST.get('company_phone')
                customer.company_email = request.POST.get('company_email')
                customer.save()
                messages.success(request, 'Profile updated successfully.')
                return redirect('customer_my_profile')
            return render(request, 'customer_my_profile.html', {'customer': customer})
        else:
            return redirect('homepage')
    else:
        return redirect('login')