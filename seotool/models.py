from django.db import models

# Create your models here.


class GoogleSearchResult(models.Model):
    query = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"
