from django import forms
from core.models import Grade

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ["value"]
