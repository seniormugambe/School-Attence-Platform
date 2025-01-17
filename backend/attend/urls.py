from django.urls import path
from .views import add_student, take_attendance, get_attendance

urlpatterns = [
    path('api/take-attendance/', take_attendance, name='take_attendance'),
    path('api/get-attendance/<int:student_id>/', get_attendance, name='get_attendance'),
    path('api/add-student/', add_student, name='add_student'),
]
