from django.db import models
from course.models.course import Course

class Video(models.Model):
   class Meta:
      db_table = 'course_video'

   title = models.CharField(max_length=255,null=False)
   course = models.ForeignKey('Course',null=False,on_delete=models.CASCADE)
   serial_number = models.IntegerField(null=False)
   video_id = models.CharField(max_length=255,null=False)
   is_preview = models.BooleanField(default=False)

   
   def __str__(self):
      return self.title

   