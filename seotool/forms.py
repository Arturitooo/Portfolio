from django import forms


class KeywordForm(forms.Form):
    keyword = forms.CharField(max_length=255)


class GenerateArticleForm(forms.Form):
    phrase = forms.CharField(max_length=255)
    article_length = forms.CharField(
        max_length=4,
        widget=forms.TextInput(attrs={"placeholder": "Characters number ex.2000"}),
    )
    other_remarks = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "Extra request ex.funny text"}),
    )
