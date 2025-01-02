from .models import MathProblem
from django import forms

class MathProblemForm(forms.ModelForm):
    class Meta:
        model = MathProblem
        fields = ['title', 'question']
        widgets = {
            'question': forms.Textarea(attrs={
                'rows': 5,
                'cols': 10,
                'class': 'w-full rounded border outline-none p-2',
                'placeholder': 'Enter your math problem here...',
            }),
            'title': forms.TextInput(attrs={
                'class': 'w-full rounded border outline-none p-2',
                'placeholder': 'Enter a title for your math problem...',
            }),
        }