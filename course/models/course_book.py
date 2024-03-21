from os import name
from django.db import models


class course_booking(models.Model):
      class Meta:
         db_table = 'course_booking'
   
      course = models.ForeignKey('Course',null=False,on_delete=models.CASCADE)
      customer = models.ForeignKey('login_registration.Customer', on_delete=models.CASCADE, default=None)
      name = models.CharField(max_length=100)
      email = models.EmailField(max_length=100)      

      def __str__(self):
         return self.course.title
