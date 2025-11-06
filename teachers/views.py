<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from core.models import Teacher, Subject, Student, Grade, Month

def teacher_login_view(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_login.html', {'teachers': teachers})

def verify_teacher_view(request):
    if request.method == 'POST':
        teacher_id = request.POST.get('teacher_id') or request.POST.get('manual_id')
        try:
            teacher = Teacher.objects.get(teacher_id=teacher_id)
            return redirect('teacher_dashboard', teacher_id=teacher.teacher_id)
        except Teacher.DoesNotExist:
            teachers = Teacher.objects.all()
            return render(request, 'teacher_login.html', {
                'teachers': teachers,
                'error': 'المعرف غير صحيح أو غير موجود.'
            })
        

def teacher_dashboard_view(request, teacher_id):
    teacher = get_object_or_404(Teacher, teacher_id=teacher_id)
    subjects = Subject.objects.filter(teacher=teacher).select_related('classroom')
    return render(request, 'teacher_dashboard.html', {
        'teacher': teacher,
        'subjects': subjects
    })



from .import functions
def subject_detail_view(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    students = Student.objects.filter(classroom=subject.classroom)
    grades = Grade.objects.filter(grade_fo_subject=subject)
    heads = []
    for gr in grades:
        #n = Month.objects.filter(grade_by_month=gr)
        heads.append(get_object_or_404(Month, grade_by_month=gr).name)
    heads = functions.rafing(heads) # ازالة العناصر المكررةمن القاىمة
    
    rows = []
    for student in students:


        row = list(Grade.objects.filter(grade_fo_subject=subject, grade_fo_student=student))
        row.insert(0, student.name)
        row = functions.stariting(heads, row, "0")
        rows.append(row)
    return render(request, 'subject_detail.html', {
        "subjectname": subject.name,
        "heads":heads,
        "rows":rows,
    })

from . import forms

def edit_grade(request, student_id, subject_id, month_id):
    student = get_object_or_404(Student, id=student_id)
    subject = get_object_or_404(Subject, id=subject_id)
    month = get_object_or_404(Month, id=month_id)
    grade = get_object_or_404(Grade, grade_fo_student=student, grade_fo_subject=subject, month=month)
    if request.method == 'POST':
        form = forms.GradeForm(request.POST, request.FILES, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('subject_detail', subject_id=subject_id)
    else:
        form = forms.GradeForm(instance=student)

    return render(request, 'edit_grade.html', {
        'form': form,
        'studentname': student.name,
        'subjectname': subject.name,
        'subject_id': subject_id,
        'monthname': month.name,
    })
        
=======
from django.shortcuts import render
from .models import Teacher
# Create your views here.
def teachers(request):
    return render(request, 'teachers_index.html', {"teachers":Teacher.objects.all()})
>>>>>>> 6fc7f65ce294a700896ae8fa57defdb07d3dc74a
