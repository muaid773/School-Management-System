from django.contrib import admin
from django.urls import path
from .views import classroom, profile, students_index, edit_student
urlpatterns = [
    path('', students_index, name="students_index"),
    path('class/<int:level_order>/', classroom, name='classroom'),
    path('profile/<int:student_id>/', profile, name='profile'),
    path('edit_profile/edit/<int:student_id>/', edit_student, name='edit_profile'),
]

