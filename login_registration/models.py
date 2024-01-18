from django.contrib.auth.models import User
from django.db import models

# Customer Model
class Customer(models.Model):

    class Meta:
        db_table = 'customer'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,default='')
    last_name = models.CharField(max_length=100,default='')
    email = models.EmailField(default='' )
    address = models.CharField(max_length=255,null = True,default = 'Default address' )
    phone = models.CharField(max_length=15,default='')

# Employee model
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    class Meta:
        db_table = 'employee'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default='')
    email = models.EmailField(default='' )
    address = models.CharField(max_length=255,null = True,default = 'Default address' )
    phone = models.CharField(max_length=15,default='')

    def __str__(self):
        return self.name 