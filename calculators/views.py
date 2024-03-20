from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def Calculators(request):
    return render(request,"calculators.html")

def income_tax_calculator(request):
    return render(request,"income-tax.html")

def sip_calculator(request):
    return render(request,"sip-calculator.html")

def gst_calculator(request):
    return render(request,"gst-calculator.html")