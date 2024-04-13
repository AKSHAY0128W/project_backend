from django.shortcuts import render,redirect 
from django.http import HttpResponse
from course.models import Course
from login_registration.models import Customer, Profile
from course.models import course_booking as CourseBooking

from django.shortcuts import render, redirect, get_object_or_404

def course_home(request):
    courses = Course.objects.all()
    booked_courses = []

    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        customer = get_object_or_404(Customer, profile=profile)
        booked_course_bookings = CourseBooking.objects.filter(customer=customer)
        booked_courses = [booking.course for booking in booked_course_bookings]

    context = {
        'courses': courses,
        'booked_courses': booked_courses,
    }

    return render(request, 'course/course_home.html', context)


def payment_page(request):
   return render(request, 'payment.html')
   