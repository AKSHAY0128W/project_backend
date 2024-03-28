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

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'indexregister.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'indexregister.html')

        if password1 != password2:
            pass

        try:
            validate_password(password1)
        except ValidationError as e:
            pass

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        profile = Profile(user=user, user_type='customer')
        profile.save()

        customer = Customer(profile=profile, name=name, address=address, phone=phone, email=email)
        customer.save()

        return redirect ('login')

    return render(request, 'indexregister.html')
from django.contrib import messages

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