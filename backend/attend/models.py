from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=50)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)  # QR code for the student
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  # Student's profile image

    def __str__(self):
        return self.name


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)  # Date when the attendance is marked
    time = models.TimeField(auto_now_add=True)  # Exact time when attendance is marked
    image = models.ImageField(upload_to='attendance_images/', blank=True, null=True)  # Optional image at the time of attendance marking
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
        ('Excused', 'Excused'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Present')

    def __str__(self):
        return f"{self.student.name} - {self.date} {self.time}"



    