from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib import admin

class Student(models.Model):
    GRADE_CHOICES = [(str(i), f"Grade {i}") for i in range(1, 13)]

    student_id = models.IntegerField(
        unique=True,
        validators=[
            MinValueValidator(10000000),
            MaxValueValidator(99999999)
        ],
        verbose_name="الرقم التعريفي"
    )
    name = models.CharField(max_length=100, verbose_name="اسم الطالب")
    age = models.PositiveIntegerField(verbose_name="العمر")
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, verbose_name="الفصل")
    email = models.EmailField(blank=True, null=True, verbose_name="البريد الإلكتروني")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="رقم الهاتف")
    address = models.TextField(blank=True, null=True, verbose_name="العنوان")
    enrollment_date = models.DateField(auto_now_add=True, verbose_name="تاريخ التسجيل")
    is_active = models.BooleanField(default=True, verbose_name="طالب نشط")

    def __str__(self):
        return f"{self.name} ({self.student_id})"

class StudentGrade(models.Model):
    student = models.OneToOneField('Student', on_delete=models.CASCADE, related_name='grades')

    quran = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="قرءان")
    islamic = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="اسلامية")
    arabic = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="عربي")
    math = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="رياضيات")
    physics = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="فيزياء")
    chemistry = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="كيمياء")
    biology = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="احياء")
    english = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="انحليزي")
    behavior = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="سلوك")

    notes = models.TextField(blank=True, null=True, verbose_name="Additional Notes")

    def __str__(self):
        return f"Grades for {self.student.name}"

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'grade', 'age', 'is_active')

@admin.register(StudentGrade)
class StudentGradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'quran', 'math', 'english', 'behavior')
