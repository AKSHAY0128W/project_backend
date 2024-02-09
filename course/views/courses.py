from django.shortcuts import render,redirect 
from django.http import HttpResponse
from course.models import Course,Video
from django.shortcuts import get_object_or_404

def coursePage(request , slug):
    course = Course.objects.get(slug  = slug)
    serial_number  = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")

    if serial_number is None:
        serial_number = 1 

    video = Video.objects.get(serial_number = serial_number , course = course)
    if ((request.user.is_authenticated is False) and (video.is_preview is False) ):
        return redirect("login")
        
    context = {
        "course" : course , 
        "video" : video , 
        'videos':videos
    }
    return  render(request , template_name="course/coursePage.html" , context=context ) 