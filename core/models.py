from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class ClassRoom(models.Model):
    name = models.CharField(max_length=20,unique=True,)
    order = models.PositiveIntegerField(unique=True, validators=[
                                        MinValueValidator(1),
                                        MaxValueValidator(12)
                                        ], verbose_name="المستوى")
    class Meta:
        ordering = ["order", "name"]
        verbose_name = "صف دراسي"
        verbose_name_plural = "صفوف دراسية"
    def __str__(self):
        return f"{self.name} [{self.order}]"
    
class Student(models.Model):
    student_id = models.IntegerField(
        unique=True,
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(99999999)
        ],
        verbose_name="الرقم التعريفي"
        )
    name = models.CharField(max_length=30,unique=True, verbose_name="الاسم")
    classroom = models.ForeignKey(ClassRoom, null=False, blank=False, on_delete=models.CASCADE, verbose_name="الصف")
    date_of_birth = models.DateField(null=False, verbose_name="تاريخ الميلاد")
    email = models.EmailField(null=False, verbose_name="البريد الاكتروني")
    photo = models.ImageField(verbose_name="صورة", null=True, blank=True, upload_to="students/photos/")
    class Meta:
        ordering = ["classroom", "name"]
        verbose_name = "طالب"
        verbose_name_plural = "طلاب"

    def __str__(self):
        return f"{self.name} ({self.student_id})"
    
class Teacher(models.Model):
    teacher_id = models.IntegerField(
        unique=True,
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(99999999)
        ],
        verbose_name="الرقم التعريفي"
        )
    name = models.CharField(max_length=30,unique=True, verbose_name="الاسم")
    def __str__(self):
        return f"{self.name} ({self.teacher_id})"

class Subject(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="المادة")
    classroom = models.ForeignKey(ClassRoom, null=False, blank=False, on_delete=models.CASCADE, verbose_name="الصف", related_name="subjects_by_classroom")
    teacher = models.ForeignKey(Teacher, null=False, blank=False, on_delete=models.CASCADE, verbose_name="المدرس", related_name="subjects_by_teacher")

    def __str__(self):
        return f"{self.name} ({self.classroom})"
    
class Month(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="الشهر")
    order = models.PositiveIntegerField(unique=True, validators=[
                                        MinValueValidator(1),
                                        MaxValueValidator(12)
                                        ], verbose_name="المستوى")
    
    def __str__(self):
        return f"{self.name}--{self.order}"
    
    class Meta:
        ordering = ["order", "name"]
        verbose_name = "شهر"
        verbose_name_plural = "شهور"

class Grade(models.Model):
    grade_fo_student = models.ForeignKey(Student, null=False, blank=False, on_delete=models.CASCADE, verbose_name="الطالب", related_name="grade_by_student")
    grade_fo_subject = models.ForeignKey(Subject, null=False, blank=False, on_delete=models.CASCADE, verbose_name="المادة", related_name="grade_by_subject")
    year = models.PositiveIntegerField(default=timezone.now().year, verbose_name='السنة')
    month = models.ForeignKey(Month, null=False, blank=False, on_delete=models.CASCADE, related_name="grade_by_month")
    value = models.FloatField(
            verbose_name="الدرجة",
            validators=[MinValueValidator(0), MaxValueValidator(100)],
            help_text="أدخل الدرجة من 0 إلى 100" )

    def __str__(self):
        return f"{self.month}-{self.grade_fo_subject}- %{self.value}"

    
    class Meta:
        verbose_name = "درجة"
        verbose_name_plural = "درجات"
        unique_together = ('grade_fo_student', 'grade_fo_subject', 'month', 'year')
        ordering = ['year', 'month', 'value']


class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='students/photos/', blank=True, null=True)
    hobbies = models.TextField(blank=True, null=True)
    registration_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=[('active', 'نشط'), ('inactive', 'منسحب')], default='active')

    def __str__(self):
        return f"بروفايل {self.student.name}"
