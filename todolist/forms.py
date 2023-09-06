from django import forms
from django.forms import DateInput, Textarea
from .models import Todos


class TodosForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = ["todopoint", "date"]
        widgets = {
            "todopoint": Textarea(
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
