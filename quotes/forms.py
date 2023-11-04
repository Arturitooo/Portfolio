# forms.py
from django import forms


class Favourite_quoteForm(forms.ModelForm):
    quote = forms.CharField(max_length=1500)
