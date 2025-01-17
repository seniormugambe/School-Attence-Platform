

from django.contrib import admin
from .models import Student,Attendance

admin.site.register(Student)  # Simple registration without customization
admin.site.register(Attendance)