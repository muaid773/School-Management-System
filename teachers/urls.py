from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_login_view, name='teacher_login'),
    path('verify/', views.verify_teacher_view, name='verify_teacher'),
    path('<int:teacher_id>/dashboard/', views.teacher_dashboard_view, name='teacher_dashboard'),
    path('subjects/<int:subject_id>/', views.subject_detail_view, name='subject_detail'),
    path('edit_grade/<int:student_id>/<int:subject_id>/<int:month_id>/', views.edit_grade, name='edit_grade'),
    path('edit_all_grades/<int:student_id>/', views.edit_all_grades, name='edit_all_grades'),

]
