from django.contrib import admin
from .models import Keywords_suggestion


class Keyword_suggestionAdmin(admin.ModelAdmin):
    # Customize how the items are displayed in the admin list
    list_display = ("title", "author", "publication_date")


# Register your models here.
admin.site.register(Keywords_suggestion)
