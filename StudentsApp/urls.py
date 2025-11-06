from django.contrib import admin
from django.urls import path
from .views import students, profile, students_index, edit_student
urlpatterns = [
    path('', students_index, name="students_index"),
    path('class/<int:level_order>/', students, name='students_table'),
    path('profile/<int:student_id>/', profile, name='profile'),
    path('students/edit/<int:student_id>/', edit_student, name='student_edit'),
]

