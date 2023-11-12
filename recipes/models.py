from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver

CUISINE_COUNTRIES = [
    ("Polish", "Polish"),
    ("German", "German"),
    ("Italian", "Italian"),
    ("French", "French"),
    ("American", "American"),
    ("Spanish", "Spanish"),
    ("Japanese", "Japan"),
    ("Indian", "Indian"),
    ("Other", "Other"),
]

MEALS = [
    ("Breafkfest", "Breakfast"),
    ("Brunch", "Brunch"),
    ("Dinner", "Dinner"),
    ("Supper", "Supper"),
]


# Create your models here.
class Recipe(models.Model):
    recipe_author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    recipe_name = models.CharField(max_length=250)
    time = models.IntegerField()  # hours - 1,5 should give user 1h30min
    cuisine = models.CharField(choices=CUISINE_COUNTRIES, max_length=50)
    meal_type = models.CharField(choices=MEALS, max_length=50)
    recipe_image = models.ImageField(upload_to="recipes/")

    def __str__(self):
        return f"{self.recipe_author} - {self.recipe_name} - {self.pk}"


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    amount = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.recipe} - {self.name}"


class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step = models.CharField(max_length=50)
    description = models.CharField(max_length=1500)

    def __str__(self):
        return f"{self.recipe} - {self.step_number}"

@receiver(pre_delete, sender=Recipe)
def delete_recipe(sender, instance, **kwargs):
    # Delete the associated image file when a Recipe is deleted
    instance.recipe_image.delete(False)