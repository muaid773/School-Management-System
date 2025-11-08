from django import forms
from django.forms import modelformset_factory

from core.models import Grade

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ["id", "value"]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }