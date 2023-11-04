from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Favourite_quote(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    quote = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.author} quote {self.pk}"
