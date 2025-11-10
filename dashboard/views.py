from django.shortcuts import render
from core.models import Student, Subject, Teacher
# Create your views here.
def main_dashboard(request):
    return render(request, 'dashboard_page.html',
                  {'teachers_len':Teacher.objects.all().count(),
                   'teachers_len_active':Teacher.objects.all().filter(is_active=True).count(),
                   'students_len':Student.objects.all().count(),
                   'students_len_active':Student.objects.all().filter(active=True).count(),
                   'subjects_len':Subject.objects.all().count(),
                   })
