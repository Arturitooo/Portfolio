from django.urls import path
from . import views

urlpatterns = [
    path("", views.seotool, name="seotool"),
    path("keyword-suggestions/", views.keyword_suggestions, name="keyword_suggestions"),
]
