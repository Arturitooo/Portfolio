from django import forms


class GoogleSearchForm(forms.Form):
    query = forms.CharField(max_length=255)
