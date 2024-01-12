from django.shortcuts import render

# Create your views here.
def default(request):
    return render(request, 'default.html')

def homepage(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def appointment(request):
    return render(request, 'appointment.html')

def dashboard(request):
    return render(request, 'customer.html')