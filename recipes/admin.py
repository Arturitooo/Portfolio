from django.contrib import admin
from .models import Recipe, Favorite_recipe, Ingredient, Instruction, RecipeRating

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Favorite_recipe)
admin.site.register(Ingredient)
admin.site.register(Instruction)
admin.site.register(RecipeRating)