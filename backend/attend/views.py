from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .models import Student, Attendance
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.decorators.csrf import csrf_exempt


import json


@csrf_exempt
def take_attendance(request):
    if request.method == "POST":
        data = json.loads(request.body)
        subject_id = data.get('subject_id')
        student_ids = data.get('student_ids')
        status_list = data.get('status_list')

        attendance_objs = [
            Attendance(subject_id=subject_id, student_id=sid, status=status)
            for sid, status in zip(student_ids, status_list)
        ]
        Attendance.objects.bulk_create(attendance_objs)
        return JsonResponse({'message': 'Attendance marked successfully'}, status=201)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_attendance(request, student_id):
    attendance_records = Attendance.objects.filter(student_id=student_id).values()
    return JsonResponse(list(attendance_records), safe=False)



@csrf_exempt
def add_student(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get('name')
        student_class = data.get('student_class')
        email = data.get('email', '')  # Optional email field

        student = Student(name=name, student_class=student_class, email=email)
        student.save()

        return JsonResponse({'message': 'Student added successfully', 'id': student.id}, status=201)

    return JsonResponse({'error': 'Invalid request'}, status=400)
