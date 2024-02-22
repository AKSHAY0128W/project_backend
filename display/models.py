from django.db import models

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
    date = models.DateField()
    time = models.TimeField()
    customer = models.ForeignKey('login_registration.Customer', on_delete=models.CASCADE, default=None)
    service = models.ForeignKey(Services, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.name

class Packages(models.Model):
    class Meta:
        db_table = 'Packages'

    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    price = models.IntegerField(default=None)      


    def __str__(self):
        return self.name
    
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