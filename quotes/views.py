import requests
from django.shortcuts import render


# Create your views here.
def quote(request):
    quote_api_url = "https://quotes15.p.rapidapi.com/quotes/random/"
    headers = {
        "X-RapidAPI-Key": "b95c0afd6cmsh72e97bad0388b66p13ad1bjsn0b1093e0e4ce",
        "X-RapidAPI-Host": "quotes15.p.rapidapi.com",
    }
    response = requests.get(quote_api_url, headers=headers)
    data = response.json()
    return render(request, "quotes/index.html", context={"data": data})
