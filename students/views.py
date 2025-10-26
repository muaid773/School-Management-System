from django.shortcuts import render, get_object_or_404
from .models import Student , StudentGrade

def students(request):
    students = Student.objects.all()
    return render(request, 'students/student_index.html', {'students': students})

def student_grades(request):
    grades = StudentGrade.objects.select_related('student').all()
    return render(request, 'students/student_grades.html', {'grades': grades})
