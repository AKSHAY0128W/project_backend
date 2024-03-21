from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.shortcuts import render
from course.models import Course, course_booking
from login_registration.models import Profile
def course_booking_view(request, id):
    selected_course = get_object_or_404(Course, id=id)

    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return HttpResponse('Profile does not exist', status=404)

    customer = profile.customer  

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        booking = course_booking(customer=customer,name=name, email=email, course=selected_course)
        booking.save()
        return redirect('homepage')

    return render(request, 'course/course_book.html', {'selected_course': selected_course})


def customer_my_courses(request):
    profile = get_object_or_404(Profile, user=request.user)
    customer = profile.customer
    booked_courses_ids = course_booking.objects.filter(customer=customer).values_list('course__id', flat=True)
    courses = Course.objects.filter(id__in=booked_courses_ids)
    return render(request, 'customer_my_courses.html', {'courses': courses})