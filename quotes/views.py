import requests
import time
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import Favourite_quoteForm
from .models import Favourite_quote


# Create your views here.
@login_required
def quote(request):
    quote_api_url = "https://quotes15.p.rapidapi.com/quotes/random/"
    headers = {
        "X-RapidAPI-Key": "b95c0afd6cmsh72e97bad0388b66p13ad1bjsn0b1093e0e4ce",
        "X-RapidAPI-Host": "quotes15.p.rapidapi.com",
    }
    content = ""
    author = ""

    # favourite_quote = Favourite_quote(user=request.user, quote=content, author=author)
    if request.method == "POST" and "add_favourite" in request.POST:
        quote = request.POST.get("content")
        author = request.POST.get("author")
        favourite_quote = Favourite_quote(user=request.user, quote=quote, author=author)
        favourite_quote.save()
        return redirect("quote")

    list_favourite_quotes = Favourite_quote.objects.filter(user=request.user)
    if len(list_favourite_quotes) < 1:
        list_favourite_quotes = None

    while len(content) < 3 or len(author) < 2:
        # loop that makes sure user will get a result - not an empty view
        response = requests.get(quote_api_url, headers=headers)
        data = response.json()
        content = data["content"]
        author = data["originator"]["name"]
        # timer added due to API limitations -
        time.sleep(0.25)

    time.sleep(0.25)
    return render(
        request,
        "quotes/index.html",
        context={
            "content": content,
            "author": author,
            "Favourite_quoteForm": Favourite_quoteForm,
            "list_favourite_quotes": list_favourite_quotes,
        },
    )


def delete_favourite_quote(request, favourite_quote_pk):
    favourite_quote = get_object_or_404(Favourite_quote, pk=favourite_quote_pk)
    if request.method == "POST":
        favourite_quote.delete()
        return redirect("quote")

    return render(
        request,
        "quotes/delete_favourite_quote.html",
        {"favourite_quote": favourite_quote},
    )
