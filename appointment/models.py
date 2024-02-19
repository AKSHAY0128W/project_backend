from django.db import models


class Appointment(models.Model):
    class Meta:
        db_table = 'appointment'

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(max_length=1000,null=True)

    def __str__(self):
        return self.name