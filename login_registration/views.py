from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm,LoginForm,CustomerForm,EmployeeForm,EmployeeDetailsForm
from django.contrib.auth.models import auth

#Customer registration view
def register(request):
    user_form = CreateUserForm()
    customer_form = CustomerForm()
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        customer_form = CustomerForm(request.POST)

        if user_form.is_valid() and customer_form.is_valid(): 
            user = user_form.save()
            customer = customer_form.save(commit=False)
            customer.user = user  
            customer.save()
            return redirect('login')

    context = {'registerform': user_form, 'customerform': customer_form}
    return render(request, 'indexregister.html', context=context)

#Login View both customer and employee and admin
def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                if user.is_superuser:
                    return redirect('admin_dashboard')
                elif user.is_staff:
                    return redirect('employee_panel')
                else:
                    return redirect('homepage')
    context = {'loginform':form}
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