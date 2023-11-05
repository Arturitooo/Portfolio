from django.db import models
from django.contrib.auth.models import User


class Keywords_suggestion(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    base_keyword = models.CharField(max_length=150)
    keywords_suggested = models.CharField(max_length=10000)
    publication_date = models.DateField()

    def __str__(self):
        return f"{self.author} - {self.base_keyword} - {self.pk}"
