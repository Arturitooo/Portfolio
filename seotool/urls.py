from django.urls import path
from . import views

urlpatterns = [
    path("", views.seotool, name="seotool"),
    path("keyword-suggestions/", views.keyword_suggestions, name="keyword_suggestions"),
    path(
        "keyword-suggestions/history/<int:pk>/",
        views.keyword_suggestions_history,
        name="keyword_suggestions_history",
    ),
]
