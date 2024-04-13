from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.shortcuts import render
from course.models import Course, course_booking
from login_registration.models import Profile
from django.shortcuts import render, redirect, get_object_or_404
from course.models import Course
from login_registration.models import Customer
from course.models import course_booking as CourseBooking

def course_booking(request, id):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login page if user is not authenticated

    course = get_object_or_404(Course, id=id)  # Get the course or return a 404 error if it doesn't exist

    profile = get_object_or_404(Profile, user=request.user)  # Get the profile associated with the current user
    customer = get_object_or_404(Customer, profile=profile)  # Get the customer associated with the profile

    CourseBooking.objects.create(customer=customer, course=course)  # Create a new CourseBooking instance

    return redirect('course_home')  # Redirect to the course home page

def customer_my_courses(request):
    profile = get_object_or_404(Profile, user=request.user)
    customer = profile.customer
    booked_courses_ids = CourseBooking.objects.filter(customer=customer).values_list('course__id', flat=True)
    courses = Course.objects.filter(id__in=booked_courses_ids)
    return render(request, 'customer_my_courses.html', {'courses': courses})