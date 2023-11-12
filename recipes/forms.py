from django import forms
from .models import Recipe, Instruction, Ingredient, Favorite_recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "recipe_name",
            "time",
            "cuisine",
            "meal_type",
            "recipe_image",
        ]

class FavoriteRecipeForm(forms.ModelForm):
    class Meta:
        model = Favorite_recipe
        fields = ['user','recipe']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            "name",
            "amount",
        ]


class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = [
            "step",
            "description",
        ]
