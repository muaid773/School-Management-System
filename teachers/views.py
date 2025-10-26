from django.shortcuts import render
from .models import Teacher
# Create your views here.
def teachers(request):
    return render(request, 'teachers_index.html', {"teachers":Teacher.objects.all()})