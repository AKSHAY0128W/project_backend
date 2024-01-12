from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm,LoginForm,CustomerForm
from django.contrib.auth.models import auth

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
                return redirect('homepage')
    context = {'loginform':form}
    return render(request, 'indexlogin.html', context=context)

def logout_view(request):
    auth.logout(request)
    return redirect('default')