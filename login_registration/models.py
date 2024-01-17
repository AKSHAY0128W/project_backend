from django.contrib.auth.models import User
from django.db import models

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,default='')
    last_name = models.CharField(max_length=100,default='')
    email = models.EmailField(default='' )
    address = models.CharField(max_length=255,null = True,default = 'Default address' )
    phone = models.CharField(max_length=15,default='')

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,default='')
    last_name = models.CharField(max_length=100,default='')
    email = models.EmailField(default='' )
    address = models.CharField(max_length=255,null = True,default = 'Default address' )
    phone = models.CharField(max_length=15,default='')
    