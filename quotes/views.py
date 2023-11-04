import requests
import time
from django.shortcuts import render
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
    while len(content) < 3 or len(author) < 2:
        # loop that makes sure user will get a result - not an empty view
        response = requests.get(quote_api_url, headers=headers)
        data = response.json()
        content = data["content"]
        author = data["originator"]["name"]
        # timer added due to API limitations -
        time.sleep(0.25)
    if request.method == "POST":
        form = Favourite_quoteForm(request.POST)
        if form.is_valid():
            Favourite_quote.objects.create(user=request.user, quote=quote)

        else:
            form = Favourite_quoteForm()
    time.sleep(0.25)
    return render(
        request,
        "quotes/index.html",
        context={
            "content": content,
            "author": author,
            "Favourite_quoteForm": Favourite_quoteForm,
        },
    )
