from django.contrib import admin
from login_registration.models import Employee, Customer
from .models import *
# Register your models here.

admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(serviceBooking)
admin.site.register(Services)