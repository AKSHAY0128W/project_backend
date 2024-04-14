from django.contrib import admin
from login_registration.models import *
from .models import *
# Register your models here.

admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(serviceBooking)
admin.site.register(PackageBooking)
admin.site.register(Services)
admin.site.register(employee_service_schedule)
admin.site.register(employee_package_schedule)  