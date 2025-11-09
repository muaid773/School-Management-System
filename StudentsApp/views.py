from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from collections import defaultdict
from core.models import Student, Grade, ClassRoom, Month

# Create your views here.
def students_index(request):
    classes =  ClassRoom.objects.all()
    return render(request, 'students_index.html', {'classes': classes})


def classroom(request, level_order):
    classroom = ClassRoom.objects.filter(order=level_order).first()
    if not classroom:
        return render(request, 'student_table.html', {'students': [], 'classroom': None})
    
    students = Student.objects.filter(classroom=classroom)
    return render(request, 'student_table.html', {'students': students, 'classroom': classroom})

def profile(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    student_grades = Grade.objects.filter(grade_fo_student=student)

    subjects = sorted(set(g.grade_fo_subject for g in student_grades), key=lambda s: s.name)
    months = sorted(set(g.month for g in student_grades), key=lambda m: m.order)

    # حساب معدل الطالب بالنسبة لعدد المواد الي يدرسها وعدد الشهور الي درسها
    allreat = ( sum(  [gradev.value for gradev in student_grades]  ) / (   (len(months)*len(subjects))*100  ) ) * 100
    allreat = round(allreat, 2)

    # بناء جدول جاهز للقالب
    rows = []
    for subject in subjects:
        row = {'subject': subject}
        for month in months:
            grade = student_grades.filter(grade_fo_subject=subject, month=month).first()
            row[month.name] = grade.value if grade else '—'
        rows.append(row)

    return render(request, 'profile.html', {
        'months': months,
        'rows': rows,
        'student': student,
        'allreat':allreat,
    })

from . import forms

def edit_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)

    if request.method == 'POST':
        form = forms.StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('profile', student_id=student.student_id)
    else:
        form = forms.StudentForm(instance=student)

    return render(request, 'edit_student.html', {
        'form': form,
        'student': student
    })
