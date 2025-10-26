from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib import admin

# Create your models here.
"""
name
id
phone
classes
subject
grad

"""

class Teacher(models.Model):
    SUBJECT_CHOICES = [("quran","quran"), ("islamic", "islamic") ,( "arabic","arabic"), ("math", "math"), ("physics", "physics"), ("chemistry","chemistry"), ("biology","biology"), ("english","english"), ("Active","Active")]
    teacher_id = models.IntegerField(
        unique=True,
        validators=[
            MinValueValidator(10000000),
            MaxValueValidator(99999999)
        ],
        verbose_name="الرقم التعريفي"
    )
    name = models.CharField(max_length=100, verbose_name="اسم المدرس")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="رقم الهاتف")
    subject = models.CharField(max_length=20, null=False, choices=SUBJECT_CHOICES, verbose_name="المادة")
    is_active = models.BooleanField(default=True, verbose_name="مدرس نشط")


    def __str__(self):
        return f"{self.name} ({self.teacher_id})"
    

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'name', 'subject', 'is_active')
