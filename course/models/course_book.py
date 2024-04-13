from django.db import models
from django.utils import timezone
from login_registration.models import Customer
from course.models import Course

class course_booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purchased_date = models.DateTimeField(default=timezone.now)