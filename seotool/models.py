from django.db import models
from django.contrib.auth.models import User


class Keywords_suggestion(models.Model):
    base_keyword = models.CharField(max_length=150)
    keywords_suggested = models.CharField(max_length=10000)
    publication_date = models.DateField()
