from django.contrib import admin

# Register your models here.
from course.models import Course, Learning
from course.models.video import Video

class LearningAdmin(admin.TabularInline):
      model = Learning 

class VideoAdmin(admin.TabularInline):
      model = Video

class CourseAdmin(admin.ModelAdmin):
      inlines = [LearningAdmin,VideoAdmin]

admin.site.register(Course,CourseAdmin)
admin.site.register(Video)
