from django.shortcuts import render,redirect 
from django.http import HttpResponse
from course.models import Course

def coursePage(request, slug):
    course = Course.objects.get(slug=slug)
    context = {
        'course': course,
    }
    return render(request, 'course/coursePage.html', context=context)