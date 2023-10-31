import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import KeywordForm, GenerateArticleForm
from decouple import config
import os
import openai


x_rapidAPI_host = config("X_RapidAPI_Host")
x_rapidAPI_key = config("X_RapidAPI_Key")
OPENAI_API_KEY = config("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


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
        if "kw_suggestions" in request.POST:
            form = KeywordForm(request.POST)
            if form.is_valid():
                keyword = form.cleaned_data["keyword"]
                querystring = {"q": keyword}
                url = "https://keyword-autosuggest.p.rapidapi.com/autosuggest"
                response = requests.get(url, headers=headers, params=querystring)

                context = {
                    "records": response.json()["result"],
                    "KeywordForm": KeywordForm,
                    "GenerateArticleForm": GenerateArticleForm,
                    "keyword": keyword.capitalize(),
                }
                return render(request, "seotool/keyword_suggest.html", context)

        elif "generate_article" in request.POST:
            form = GenerateArticleForm(request.POST)
            if form.is_valid():
                phrase = form.cleaned_data["phrase"]
                article_length = form.cleaned_data["article_length"]
                other_remarks = form.cleaned_data["other_remarks"]
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": "Jesteś copywriterem, który z łatwością potrafi opisać skomplikowane zagadanienia - przy tym wzbogacając tekst o wątki humorystyczne lub ciekawe historie powiązane z tematem",
                        },
                        {
                            "role": "user",
                            "content": f"Przygotuj tekst o długości {article_length} znaków (włącznie ze spacjami), który podejmie temat: {phrase}. Pamiętaj aby tekst zawierał: {other_remarks}",
                        },
                    ],
                )
                generated_article = completion.choices[0].message["content"]
                context = {
                    "KeywordForm": KeywordForm,
                    "keyword": phrase.capitalize(),
                    "generated_article": generated_article,
                }
                return render(request, "seotool/keyword_suggest.html", context)
    else:
        form = KeywordForm()

    return render(request, "seotool/keyword_suggest.html", {"KeywordForm": KeywordForm})
