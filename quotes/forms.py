# forms.py
from django import forms
from .models import Favourite_quote


class Favourite_quoteForm(forms.ModelForm):
    class Meta:
        model = Favourite_quote
        fields = ["user", "quote", "author"]
