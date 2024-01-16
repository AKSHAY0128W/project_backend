from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def Calculators(request):
    return render(request,"calculators.html")
