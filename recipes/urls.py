from django.urls import path
from .views import recipes, add_recipe, add_ingredients, added_recipe

urlpatterns = [
    path("", recipes, name="recipes"),
    path("add-recipe/", add_recipe, name="add_recipe"),
    path("add-ingredients/<int:recipe_id>/", add_ingredients, name="add_ingredients"),
    path("add/success", added_recipe, name="added_recipe"),
]
