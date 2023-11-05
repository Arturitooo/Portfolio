from django.urls import path
from . import views

urlpatterns = [
    path("", views.quote, name="quote"),
    path(
        "<int:favourite_quote_pk>/delete/",
        views.delete_favourite_quote,
        name="delete_favourite_quote",
    ),
]
