from django.db import models

class Course(models.Model):
   class Meta:
      db_table = 'course'
   
   name = models.CharField(max_length=255,null=False)
   slug = models.CharField(max_length=255,null=False,unique=True)
   description = models.CharField(max_length=255,null=False)
   price = models.IntegerField(null=False)
   discount = models.IntegerField(null=False,default=0)
   active = models.BooleanField(default=False)
   thumbnail = models.ImageField(upload_to='thumbnail')
   date = models.DateTimeField(auto_now_add=True)
   resource = models.FileField(upload_to='resources')
   length = models.IntegerField(null=False)

   def __str__(self):
      return self.name

class courseProperty(models.Model):
   description = models.CharField(max_length=255,null=False)
   Course = models.ForeignKey(Course,null = False,on_delete=models.CASCADE)

   class Meta:
      abstract = True

class Tag(courseProperty):
   class Meta:
      db_table = 'course_tag'

   pass
   
class Prerequisite(courseProperty):
   class Meta:
      db_table = 'course_prerequisite'
   
   pass
class Learning(courseProperty):
   class Meta:
      db_table = 'course_learning'
   
   pass