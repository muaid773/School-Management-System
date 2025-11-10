from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# ==========================
# ClassRoom Model
# ==========================
class ClassRoom(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="اسم الصف")
    order = models.PositiveIntegerField(
        unique=True,
        validators=[MinValueValidator(1), MaxValueValidator(12)],
        verbose_name="المستوى الدراسي"
    )

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "صف دراسي"
        verbose_name_plural = "صفوف دراسية"

    def __str__(self):
        return f"{self.name} [{self.order}]"


# ==========================
# Student Model
# ==========================
class Student(models.Model):
    student_id = models.IntegerField(
        unique=True,
        validators=[MinValueValidator(1000), MaxValueValidator(99999999)],
        verbose_name="الرقم التعريفي"
    )
    name = models.CharField(max_length=50, unique=True, verbose_name="الاسم")
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, verbose_name="الصف")
    date_of_birth = models.DateField(verbose_name="تاريخ الميلاد")
    date = models.DateField(auto_now_add=True, verbose_name="تاريه التسجيل")
    address = models.TextField(max_length=50, verbose_name="العنوان")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    photo = models.ImageField(
        verbose_name="صورة الطالب",
        upload_to="students/photos/",
        blank=True,
        null=True
    )
    active = models.BooleanField(verbose_name="نشط", auto_created=True)
    notes = models.TextField(verbose_name="ملاحظات إضافية", blank=True)

    class Meta:
        ordering = ["classroom", "name"]
        verbose_name = "طالب"
        verbose_name_plural = "طلاب"

    def __str__(self):
        return f"{self.name} ({self.student_id})"


# ==========================
# Teacher Model
# ==========================
class Teacher(models.Model):
    teacher_id = models.IntegerField(
        unique=True,
        validators=[MinValueValidator(1000), MaxValueValidator(99999999)],
        verbose_name="الرقم التعريفي"
    )
    name = models.CharField(max_length=50, unique=True, verbose_name="الاسم")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    phone = models.CharField(max_length=20, blank=True, verbose_name="رقم الهاتف")
    specialty = models.CharField(max_length=50, blank=True, verbose_name="التخصص")
    photo = models.ImageField(
        upload_to="teachers/photos/",
        blank=True,
        null=True,
        verbose_name="صورة المدرس"
    )
    bio = models.TextField(blank=True, verbose_name="معلومات إضافية عن المدرس")
    is_active = models.BooleanField(default=True, verbose_name="نشط")

    class Meta:
        ordering = ["name"]
        verbose_name = "مدرس"
        verbose_name_plural = "مدرسون"

    def __str__(self):
        return f"{self.name} ({self.teacher_id})"


# ==========================
# Subject Model
# ==========================
class Subject(models.Model):
    name = models.CharField(max_length=50, verbose_name="المادة")
    classroom = models.ForeignKey(
        ClassRoom,
        on_delete=models.CASCADE,
        verbose_name="الصف",
        related_name="subjects_by_classroom"
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        verbose_name="المدرس",
        related_name="subjects_by_teacher"
    )

    class Meta:
        verbose_name = "مادة"
        verbose_name_plural = "مواد"
        ordering = ["classroom", "name"]
        unique_together = ("name", "classroom")  # الاسم يكون فريدًا فقط داخل الصف
    def __str__(self):
        return f"{self.name} ({self.classroom})"


# ==========================
# Month Model
# ==========================
class Month(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="الشهر")
    order = models.PositiveIntegerField(
        unique=True,
        validators=[MinValueValidator(1), MaxValueValidator(12)],
        verbose_name="الترتيب"
    )

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "شهر"
        verbose_name_plural = "شهور"

    def __str__(self):
        return f"{self.name} ({self.order})"


# ==========================
# Grade Model
# ==========================
class Grade(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name="الطالب",
        related_name="grades"
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        verbose_name="المادة",
        related_name="grades"
    )
    year = models.PositiveIntegerField(default=timezone.now().year, verbose_name="السنة")
    month = models.ForeignKey(
        Month,
        on_delete=models.CASCADE,
        verbose_name="الشهر",
        related_name="grades"
    )
    value = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="الدرجة",
        help_text="أدخل الدرجة من 0 إلى 100"
    )

    class Meta:
        verbose_name = "درجة"
        verbose_name_plural = "درجات"
        unique_together = ("student", "subject", "month", "year")
        ordering = ["year", "month", "subject", "value"]

    def __str__(self):
        return f"{self.student} - {self.subject} [{self.month}] : {self.value}%"
