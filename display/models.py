from django.db import models

# Create your models here.

class Services(models.Model):
    class Meta:
        db_table = 'Services'

    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='services/',max_length=1000,null=True,default=None)
    description = models.TextField()
    price = models.IntegerField(default=None)

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