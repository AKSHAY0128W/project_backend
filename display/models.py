from email.policy import default
from django.db import models
from django.utils import timezone
import login_registration
from datetime import timedelta
# Create your models here.

class Services(models.Model):
    class Meta:
        db_table = 'Services'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='services/',max_length=1000,null=True,default=None)
    description = models.TextField()
    price = models.IntegerField(default=None)

    def __str__(self):
        return self.name
    
class serviceBooking(models.Model):
    class Meta:
        db_table = 'service_booking'
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default=None)
    email = models.EmailField(null = True, default=None)
    phone = models.CharField(max_length=10, default=None)    
    date = models.DateField()
    time = models.TimeField()
    customer = models.ForeignKey('login_registration.Customer', on_delete=models.CASCADE, default=None)
    service = models.ForeignKey(Services, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.name
    
class employee_service_schedule(models.Model):
    class Meta:
        db_table = 'employee_service_schedule'

    service_schedule_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey('login_registration.Employee', on_delete=models.CASCADE)
    servbooking = models.ForeignKey(serviceBooking, on_delete=models.CASCADE)  # Changed booking to servbooking
    datetime = models.DateTimeField(default=timezone.now)


class Packages(models.Model):
    class Meta:
        db_table = 'Packages'

    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    price = models.IntegerField(default=None)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
    

class PackageBooking(models.Model):
    class Meta:
        db_table = 'package_booking'
    
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now);
    duration = models.CharField(max_length=100,default=None)
    customer = models.ForeignKey('login_registration.Customer', on_delete=models.CASCADE, default=None)
    package = models.ForeignKey(Packages, on_delete=models.CASCADE, default=None)
    def end_date(self):
        return self.date + timedelta(days=int(self.duration))
    def __str__(self):
        return self.name
    
class employee_package_schedule(models.Model):
    class Meta:
        db_table = 'employee_package_schedule'

    package_schedule_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey('login_registration.Employee', on_delete=models.CASCADE)
    packbooking = models.ForeignKey(PackageBooking, on_delete=models.CASCADE)  # Changed booking to packbooking
    datetime = models.DateTimeField(default=timezone.now)
    
class payment(models.Model):
    class Meta:
        db_table = 'payment'
    
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    customer = models.ForeignKey('login_registration.Customer', on_delete=models.CASCADE, default=None)
    service = models.ForeignKey(Services, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return str(self.id)
    
