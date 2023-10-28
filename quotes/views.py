import requests
import time
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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
        time.sleep(0.5)
    print(content, author)
    time.sleep(0.5)
    return render(
        request, "quotes/index.html", context={"content": content, "author": author}
    )
