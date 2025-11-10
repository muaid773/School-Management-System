from django.shortcuts import render, get_object_or_404, redirect
from collections import defaultdict
from core.models import Student, Grade, ClassRoom, Month
from . import forms

# Display list of all classrooms
def students_index(request):
    classes = ClassRoom.objects.all()
    return render(request, 'students_index.html', {'classes': classes})


# Display students in a specific classroom by its order/level
def classroom(request, level_order):
    classroom = ClassRoom.objects.filter(order=level_order).first()
    if not classroom:
        return render(request, 'student_table.html', {'students': [], 'classroom': None})
    
    students = Student.objects.filter(classroom=classroom)
    return render(request, 'student_table.html', {'students': students, 'classroom': classroom})


# Display detailed profile and grades of a specific student
def profile(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    student_grades = Grade.objects.filter(student=student)

    # Get unique subjects and months, sorted by name and order
    subjects = sorted(set(g.subject for g in student_grades), key=lambda s: s.name)
    months = sorted(set(g.month for g in student_grades), key=lambda m: m.order)

    # Calculate overall student average based on all subjects and months
    total_grades = sum(grade.value for grade in student_grades)
    max_total = len(months) * len(subjects) * 100
    if max_total > 0:
        allreat = round((total_grades / max_total) * 100, 2)
    else:
        allreat = 0


    # Build table rows for template
    rows = []
    for subject in subjects:
        row = {'subject': subject}
        for month in months:
            grade = student_grades.filter(subject=subject, month=month).first()
            row[month.name] = grade.value if grade else '—'
        rows.append(row)

    return render(request, 'profile.html', {
        'months': months,
        'rows': rows,
        'student': student,
        'allreat': allreat,
    })


# Edit student information
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
