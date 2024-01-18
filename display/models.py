from django.db import models

# Create your models here.

class Services(models.Model):
    class Meta:
        db_table = 'Services'

    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='services/',max_length=1000,null=True,default=None)
    description = models.TextField()

    def __str__(self):
        return self.name