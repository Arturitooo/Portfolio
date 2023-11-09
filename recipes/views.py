from django.shortcuts import render, redirect
from .forms import RecipeForm, IngredientForm, InstructionForm
from .models import Recipe


# Create your views here.
def recipes(request):
    # search
    # list of recipes
    # recipe details page
    # add to favourite
    # comment recipe
    # rate recipe
    return render(request, "recipes/index.html")


def add_recipe(request):
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.recipe_author = request.user
            recipe.save()
            return redirect("recipes/add_ingredients", recipe_id=recipe.id)
    else:
        recipe_form = RecipeForm()

    return render(request, "recipes/add_recipe.html", {"recipe_form": recipe_form})


def add_ingredients(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)

    if request.method == "POST":
        ingredient_form = IngredientForm(request.POST)
        if ingredient_form.is_valid():
            ingredient = ingredient_form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()
            return redirect("recipes/add_ingredients", recipe_id=recipe.id)
    else:
        ingredient_form = IngredientForm()

    return render(
        request,
        "recipes/add_ingredients.html",
        {"ingredient_form": ingredient_form, "recipe": recipe},
    )


def added_recipe(request):
    # RecipeCreateView success page
    return render(request, "recipes/added_recipe.html")
