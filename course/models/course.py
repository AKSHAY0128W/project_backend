from django.db import models
from django.utils import timezone

class Course(models.Model):
   class Meta:
      db_table = 'course'
   
   name = models.CharField(max_length=255,null=False)
   slug = models.CharField(max_length=255,null=False,unique=True)
   description = models.CharField(max_length=255,null=False,default='')
   price = models.IntegerField(null=False)
   discount = models.IntegerField(null=False,default=0)
   thumbnail = models.ImageField(upload_to='thumbnail')
   date = models.DateTimeField(default=timezone.now)
   resource = models.FileField(upload_to='resources')

   

   def __str__(self):
      return self.name

class Learning(models.Model):
   class Meta:
      db_table = 'course_learning'
   
   learning_description = models.CharField(max_length=255,null=False)
   course = models.ForeignKey(Course,null=False,on_delete=models.CASCADE)
