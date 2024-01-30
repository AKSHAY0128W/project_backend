from django.contrib import admin

# Register your models here.
from course.models import Course, Tag, Prerequisite, Learning
from course.models.video import Video
class TagAdmin(admin.TabularInline):
      model = Tag

class PrerequisiteAdmin(admin.TabularInline):     
      model = Prerequisite

class LearningAdmin(admin.TabularInline):
      model = Learning 

class VideoAdmin(admin.TabularInline):
      model = Video

class CourseAdmin(admin.ModelAdmin):
      inlines = [TagAdmin,PrerequisiteAdmin,LearningAdmin,VideoAdmin]

admin.site.register(Course,CourseAdmin)
admin.site.register(Video)
