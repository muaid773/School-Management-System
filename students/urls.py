from django.urls import path
from . import views

urlpatterns = [
    path('', views.students, name='index'),
    path('grades', views.student_grades, name='grades'),
]