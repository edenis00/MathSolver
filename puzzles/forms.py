from .models import MathProblem
from django import forms

class MathProblemForm(forms.ModelForm):
    class Meta:
        model = MathProblem
        fields = ['question', 'solution']