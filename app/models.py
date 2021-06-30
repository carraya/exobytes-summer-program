from django.db import models
from django.contrib.auth.models import User
# from django.db.models.deletion import CASCADE

COURSE_CHOICES = [
    ("SS", "Subsystems"),
    ("M1", "Motion Level 1"),
    ("M2", "Motion Level 2"),
]

class CourseType(models.Model):
    course_name = models.CharField(max_length=14, choices=COURSE_CHOICES, default="SS")

    def __str__(self):
        return self.course_name

