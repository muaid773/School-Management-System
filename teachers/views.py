from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from core.models import Teacher, Subject, Student, Grade, Month
from . import forms
from django.forms import modelformset_factory, formset_factory


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
        heads.append(gr.month.name)
    heads = functions.rafing(heads) # ازالة العناصر المكررةمن القاىمة
    
    rows = []
    for student in students:


        row = [student] + list(Grade.objects.filter(grade_fo_subject=subject, grade_fo_student=student))
        row = functions.stariting(heads, row, "0")
        rows.append(row)
    return render(request, 'subject_detail.html', {
        'month': 1,
        "subjectname": subject.name,
        "heads":heads,
        "rows":rows,
    })




def edit_grade(request, student_id, subject_id, month_id):
    student = get_object_or_404(Student, id=student_id)
    subject = get_object_or_404(Subject, id=subject_id)
    month = get_object_or_404(Month, id=month_id)
    grade = get_object_or_404(Grade, grade_fo_student=student, grade_fo_subject=subject, month=month)
    if request.method == 'POST':
        form = forms.GradeForm(request.POST, request.FILES, instance=grade)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('subject_detail', subject_id=subject_id)
    else:
        form = forms.GradeForm(instance=grade)

    return render(request, 'edit_grade.html', {
        'form': form,
        'studentname': student.name,
        'subjectname': subject.name,
        'subject_id': subject_id,
        'monthname': month.name,
    })



"""def edit_all_grades(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    grades = Grade.objects.filter(grade_fo_student=student)
    GradeFormSet = modelformset_factory(Grade, form=forms.GradeForm, extra=0)
    if request.method == 'POST':
        formset = GradeFormSet(request.POST, request.FILES, queryset=grades)
        print("\n\n",formset,"\n\n",)
        print(formset.is_valid())
        if formset.is_valid():
            formset.save()
            return redirect('edit_all_grades', student_id=student.id)
    else:
        formset = GradeFormSet(queryset=grades)

    return render(request, 'edit_all_grades.html', {
        'student': student,
        'formset':formset,
    })
"""

















from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction

def edit_all_grades(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    subjects = Subject.objects.all().order_by('id')
    months = Month.objects.all().order_by('id')

    # تحويل الدرجات إلى dict بشكل يسهل الوصول
    grades = Grade.objects.filter(grade_fo_student=student)
    grade_dict = {
        (g.grade_fo_subject_id, g.month_id): g
        for g in grades
    }

    if request.method == 'POST':
        with transaction.atomic():
            for subject in subjects:
                for month in months:
                    field_name = f"grade_{subject.id}_{month.id}"
                    value = request.POST.get(field_name)
                    if value is None or value == "":
                        continue
                    value = float(value)
                    grade_obj = grade_dict.get((subject.id, month.id))
                    if grade_obj:
                        grade_obj.value = value
                        grade_obj.save()
                    else:
                        Grade.objects.create(
                            grade_fo_student=student,
                            grade_fo_subject=subject,
                            month=month,
                            year=student.year if hasattr(student, "year") else 2025,
                            value=value,
                        )
        return redirect('edit_all_grade', student_id=student.id)

    context = {
        'student': student,
        'subjects': subjects,
        'months': months,
        'grade_dict': grade_dict,
    }
    return render(request, 'edit_all_grades.html', context)
