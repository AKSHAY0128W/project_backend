from django.shortcuts import render,redirect 
from django.http import HttpResponse
from course.models import Course

def course_home(request):
   courses = Course.objects.all()
   print(courses)
   context = {
      'courses': courses
   }
   return render(request, 'course/course_home.html',context)