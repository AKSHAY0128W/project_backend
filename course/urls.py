from django.urls import path, include
from course.views import course_home, coursePage, payment_page, course_booking
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', course_home, name='course_home'),
    path('course_details/<slug:slug>/', coursePage, name='coursePage'),
    path('payment/', payment_page, name='payment_page'),
]