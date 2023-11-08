from django.shortcuts import render

# Create your views here.
def mainpage(request):
    #search
    #list of recipes
    #recipe details page
    #add to favourite
    #comment recipe
    #rate recipe
    return render(request, "recipes/index.html")