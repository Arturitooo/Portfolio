from django.db import models
from django.contrib.auth.models import User

CUISINE_COUNTRIES = [
    ("Polish", "🇵🇱"),
    ("German", "🇩🇪"),
    ("Italian", "🇮🇹"),
    ("French", "🇫🇷"),
    ("American", "🇺🇸"),
    ("Spanish", "🇪🇸"),
    ("Japanese", "🇯🇵"),
    ("Indian", "🇮🇳"),
    ("Other", ""),
]


# Create your models here.
class Recipe(models.Model):
    recipe_author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    recipe_name = models.CharField(max_length=250)
    time_consumption = models.IntegerField()  # hours - 1,5 should give user 1h30min
    cuisine = models.CharField(choices=CUISINE_COUNTRIES, max_length=25)
    recipe_image = models.ImageField(upload_to="uploads/recipes")
    guidelines = models.CharField(max_length=5000)

    def __str__(self):
        return f"{self.recipe_author} - {self.recipe_name} - {self.pk}"
