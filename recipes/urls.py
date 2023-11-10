from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import recipes, add_recipe, add_ingredients, added_recipe, add_instructions

urlpatterns = [
    path("", recipes, name="recipes"),
    path("add-recipe/", add_recipe, name="add_recipe"),
    path("add-ingredients/<int:recipe_id>/", add_ingredients, name="add_ingredients"),
    path(
        "add-instructions/<int:recipe_id>/", add_instructions, name="add_instructions"
    ),
    path("add/success/", added_recipe, name="added_recipe"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)