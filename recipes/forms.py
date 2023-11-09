from django import forms
from .models import Recipe, Instruction, Ingredient


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "recipe_name",
            "time_consumption",
            "cuisine",
            "meal_type",
            "recipe_image",
        ]


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
            "step_number",
            "description",
        ]
