import requests
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import KeywordForm, GenerateArticleForm
from .models import Keywords_suggestion
from decouple import config
from django.utils import timezone
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

    history_kw_suggestions = Keywords_suggestion.objects.filter(author=request.user)
    history_kw_suggestions = history_kw_suggestions.order_by("-pk")[:5]

    base_keywords = [
        history_kw_suggestion.base_keyword
        for history_kw_suggestion in history_kw_suggestions
    ]

    context = {"base_keywords": history_kw_suggestions, "KeywordForm": KeywordForm}

    if request.method == "POST":
        if "kw_suggestions" in request.POST:
            form = KeywordForm(request.POST)
            if form.is_valid():
                keyword = form.cleaned_data["keyword"]
                querystring = {"q": keyword}
                url = "https://keyword-autosuggest.p.rapidapi.com/autosuggest"
                response = requests.get(url, headers=headers, params=querystring)

                context = {
                    "base_keywords": history_kw_suggestions,
                    "KeywordForm": KeywordForm,
                    "records": response.json()["result"],
                    "GenerateArticleForm": GenerateArticleForm,
                    "keyword": keyword,
                }

            merged_kw_suggested = ""
            for kw_suggested_item in response.json()["result"]:
                merged_kw_suggested += kw_suggested_item + "||"

            keywords_suggestion = Keywords_suggestion(
                base_keyword=keyword,
                author=request.user,
                keywords_suggested=merged_kw_suggested,
                publication_date=timezone.now(),
            )
            keywords_suggestion.save()

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
                    "base_keywords": history_kw_suggestions,
                    "KeywordForm": KeywordForm,
                    "keyword": phrase.capitalize(),
                    "generated_article": generated_article,
                }
                return render(request, "seotool/keyword_suggest.html", context)

    return render(
        request,
        "seotool/keyword_suggest.html",
        context,
    )


@login_required
def keyword_suggestions_history(request, pk):
    keywords_suggestion = get_object_or_404(Keywords_suggestion, pk=pk)
    keywords_suggested = keywords_suggestion.keywords_suggested.rstrip("||").split("||")

    context = {
        "base_keyword": keywords_suggestion.base_keyword,
        "keywords_suggested": keywords_suggested,
    }
    return render(request, "seotool/kw_history.html", context)
