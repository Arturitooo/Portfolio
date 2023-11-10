from django.shortcuts import render, redirect
from .forms import RecipeForm, IngredientForm, InstructionForm
from .models import Recipe


# Create your views here.
def recipes(request):

    recipes = Recipe.objects.select_related('recipe_author').prefetch_related('ingredient_set', 'instruction_set').all()

    # search
    # list of recipes
    # recipe details page
    # add to favourite
    # comment recipe
    # rate recipe
    return render(request, "recipes/index.html", {'recipes': recipes})


def add_recipe(request):
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.recipe_author = request.user
            recipe.save()
            return redirect("add_ingredients", recipe_id=recipe.id)

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
            return redirect("add_ingredients", recipe_id=recipe.id)
    else:
        ingredient_form = IngredientForm()

    return render(
        request,
        "recipes/add_ingredients.html",
        {"ingredient_form": ingredient_form, "recipe": recipe},
    )


def add_instructions(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)

    if request.method == "POST":
        instruction_form = InstructionForm(request.POST)
        if instruction_form.is_valid():
            instruction = instruction_form.save(commit=False)
            instruction.recipe = recipe
            instruction.save()
            return redirect("add_instructions", recipe_id=recipe.id)
    else:
        instruction_form = InstructionForm()

    return render(
        request,
        "recipes/add_instructions.html",
        {"instruction_form": instruction_form, "recipe": recipe},
    )


# i need to differentiate when to go from step 2 to step 3 and when to ad one more items
# i need to differentiate when to go from step 3 to step thx page and when to ad one more items


def added_recipe(request):
    # RecipeCreateView success page
    return render(request, "recipes/added_recipe.html")
