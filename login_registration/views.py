from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm,LoginForm,CustomerForm,EmployeeForm,EmployeeDetailsForm
from django.contrib.auth.models import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from .models import Customer,Employee,Profile


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

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
        

        customer = Customer(profile=profile, name=name, address=address, phone=phone,email=email)
        customer.save()

        return redirect('login')

    return render(request, 'indexregister.html')

#Login View both customer and employee and admin
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')
            elif user.is_staff:
                return redirect('employee_panel')
            else:
                return redirect('homepage')
    context = {'form': LoginForm()}
    return render(request, 'indexlogin.html', context=context)
    
#Logout View for customer and employee and admin
def logout_view(request):
    auth.logout(request)
    return redirect('default')

#Employee creation view for admin
def create_employee(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = EmployeeForm(request.POST)
            edetails = EmployeeDetailsForm(request.POST)
            if form.is_valid() and edetails.is_valid():
                form.save()

                profile = Profile(user=form.instance, user_type='employee')
                profile.save()

                edetails = edetails.save(commit=False)
                edetails.profile = profile
                edetails.save()
                return redirect('admin_dashboard')
            else:
                print(form.errors, edetails.errors)
        else:
            form = EmployeeForm()
            edetails = EmployeeDetailsForm()
        context = {'eform': form, 'edetails': edetails}
        return render(request, 'admin_create_employee.html', context=context)
    else:
        return redirect('homepage')