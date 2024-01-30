from django.urls import path, include
from course.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('course_home', course_home, name='course_home'),
]