from django.shortcuts import render,redirect 
from django.http import HttpResponse
from course.models import Course,Video
from django.shortcuts import get_object_or_404


def coursePage(request, slug):
    course = get_object_or_404(Course, slug=slug)
    serial_number = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")

    if serial_number is None:
        serial_number = 1 

    video = get_object_or_404(Video, serial_number=serial_number, course=course)

    if ((request.user.is_authenticated is False) and (video.is_preview is False)):
        return redirect("login")
        
    context = {
        "course": course,
        "video": video,
        'videos': videos
    }

    return render(request, "course/coursePage.html", context)