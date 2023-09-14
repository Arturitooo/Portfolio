import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import GoogleSearchForm


# Create your views here.
@login_required
def dashboard(request):
    form = GoogleSearchForm()

    if request.method == "POST":
        form = GoogleSearchForm(request.POST)

        if form.is_valid():
            user_query = form.cleaned_data.get("query")
            # perform scrapping
            results_list = ["1", "2", "three", "4", "5ive", user_query]
            return render(
                request,
                "seotool/index.html",
                {"form": form, "results_list": results_list},
            )

    return render(request, "seotool/index.html", {"form": form})
