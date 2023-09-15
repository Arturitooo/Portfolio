from django import forms
from django.forms import DateInput, Textarea
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["task", "date"]
        widgets = {
            "task": Textarea(
                attrs={
                    "required": True,
                    "class": "form-control",
                    "style": "max-width: 400px;",
                    "placeholder": "...",
                }
            ),
            "date": DateInput(
                attrs={
                    "required": True,
                    "class": "form-control",
                    "style": "max-width: 400px;",
                    "placeholder": "yyyy-mm-dd",
                }
            ),
        }
