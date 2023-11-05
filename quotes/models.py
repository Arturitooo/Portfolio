from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Favourite_quote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    quote = models.CharField(max_length=2500)
    author = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.user} quote {self.pk}"
