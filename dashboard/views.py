from django.shortcuts import render
from core.models import Student, Subject, Teacher
# Create your views here.
def main_dashboard(request):
    return render(request, 'dashboard_page.html',
                  {'teachers':len(Teacher.object.all()),
                   'students':len(Student.object.all()),
                   'subjects':len(Subject.object.all())
                   })
