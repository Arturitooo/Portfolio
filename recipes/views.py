from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import RecipeForm, IngredientForm, InstructionForm
from .models import Recipe, Ingredient, Instruction

#TODO 
    # add to favourite
    # comment recipe
    # rate recipe
    # search in recipes

# Create your views here.
def recipes(request):
    recipes = Recipe.objects.select_related('recipe_author').prefetch_related('ingredient_set', 'instruction_set').all()
    recipes_counter = len(Recipe.objects.all())
    return render(request, "recipes/index.html", context = {'recipes': recipes,'recipes_counter': recipes_counter})

class RecipeDetailView(DetailView):
    model = Recipe

class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = [
            "recipe_name",
            "time",
            "cuisine",
            "meal_type",
            "recipe_image",
        ]
    success_url = reverse_lazy("success_page")

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = "recipes/recipe_confirm_delete.html"
    success_url = reverse_lazy("recipes")


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

class IngredientUpdateView(UpdateView):
    model = Ingredient
    fields = [
            "name",
            "amount",
        ]
    success_url = reverse_lazy("success_page")

class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = "recipes/ingredient_confirm_delete.html"
    success_url = reverse_lazy("success_page")


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

class InstructionUpdateView(UpdateView):
    model = Instruction
    fields = [
            "step",
            "description",
        ]
    success_url = reverse_lazy("success_page")

class InstructionDeleteView(DeleteView):
    model = Instruction
    template_name = "recipes/Instruction_confirm_delete.html"
    success_url = reverse_lazy("success_page")

def success_page(request):
    # RecipeCreateView success page
    return render(request, "recipes/success.html")
