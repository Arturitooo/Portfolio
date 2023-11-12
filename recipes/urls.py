from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import recipes, add_recipe, add_ingredients, success_page, add_instructions, RecipeDetailView, RecipeUpdateView, RecipeDeleteView, IngredientUpdateView, IngredientDeleteView, InstructionUpdateView, InstructionDeleteView

urlpatterns = [
    path("", recipes, name="recipes"),
    path("add-recipe/", add_recipe, name="add_recipe"),
    path("add-ingredients/<int:recipe_id>/", add_ingredients, name="add_ingredients"),
    path(
        "add-instructions/<int:recipe_id>/", add_instructions, name="add_instructions"
    ),
    path("success/", success_page, name="success_page"),
    path('recipe-detail/<int:pk>/', RecipeDetailView.as_view(), name="recipe_detail"),
    path('update-recipe/<int:pk>/', RecipeUpdateView.as_view(), name="recipe_update"),
    path('delete-recipe/<int:pk>/', RecipeDeleteView.as_view(), name="recipe_delete"),
    path('update-inredient/<int:pk>/', IngredientUpdateView.as_view(), name="ingredient_update"),
    path('delete-inredient/<int:pk>/', IngredientDeleteView.as_view(), name="ingredient_delete"),
    path('update-instruction/<int:pk>/', InstructionUpdateView.as_view(), name="instruction_update"),
    path('delete-instruction/<int:pk>/', InstructionDeleteView.as_view(), name="instruction_delete"),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)