from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe, Favorite_recipe, Ingredient, Instruction, RecipeRating

# Create your tests here.

class RecipeModelTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_recipe_creation(self):
        # Test creating a Recipe instance
        recipe = Recipe.objects.create(
            recipe_author=self.user,
            recipe_name='Test Recipe',
            time=30,
            cuisine='Italian',
            meal_type='Dinner',
            recipe_image=f'uploads\recipes\image_11.png',
            average_rating=0,
            total_ratings=0,
        )
        self.assertEqual(recipe.recipe_name, 'Test Recipe')
        self.assertEqual(recipe.recipe_author, self.user)
        self.assertEqual(recipe.meal_type, 'Dinner')
        self.assertEqual(recipe.cuisine, 'Italian')
        self.assertEqual(recipe.time, 30)

'''    def test_favorite_recipe_creation(self):
        # Test creating a Favorite_recipe instance
        favorite_recipe = Favorite_recipe.objects.create(user=self.user, recipe=self.recipe)
        self.assertEqual(favorite_recipe.user, self.user)
        self.assertEqual(favorite_recipe.recipe, self.recipe)'''