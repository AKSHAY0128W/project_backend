from django.contrib.auth.models import User
from django.db import models


# Multiuser Profile Model
class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('customer', 'customer'),
        ('employee', 'employee'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='customer')

    def __str__(self):
        return self.user.username


# Customer Model
class Customer(models.Model):
    class Meta:
        db_table = 'customer'

    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(default='', unique=True)
    address = models.CharField(max_length=255, null=True, default='Default address')
    phone = models.CharField(max_length=15, default='')

    def __str__(self):
        return self.name


# Employee model
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'employee'

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, default='')
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(default='', unique=True)
    address = models.CharField(max_length=255, null=True, default='Default address')
    phone = models.CharField(max_length=15, default='')

    def __str__(self):
        return self.name
