from django.shortcuts import render,HttpResponse,redirect


# Create your views here.


def Calculators(request):
    return render(request,"calculators.html")
