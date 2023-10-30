import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import KeywordForm
from decouple import config

x_rapidAPI_host = config("X_RapidAPI_Host")
x_rapidAPI_key = config("X_RapidAPI_Key")


# Create your views here.
@login_required
def seotool(request):
    return render(request, "seotool/index.html")


@login_required
def keyword_suggestions(request):
    headers = {
        "X-RapidAPI-Key": x_rapidAPI_key,
        "X-RapidAPI-Host": x_rapidAPI_host,
    }

    if request.method == "POST":
        form = KeywordForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data["keyword"]
            querystring = {"q": keyword}
            url = "https://keyword-autosuggest.p.rapidapi.com/autosuggest"
            response = requests.get(url, headers=headers, params=querystring)

        context = {
            "records": response.json()["result"],
            "form": KeywordForm,
            "keyword": keyword.capitalize(),
        }
        return render(request, "seotool/keyword_suggest.html", context)

    else:
        form = KeywordForm()

    return render(request, "seotool/keyword_suggest.html", {"form": KeywordForm})
