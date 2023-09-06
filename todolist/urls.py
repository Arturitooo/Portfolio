from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_todos, name="my_todos_list"),
    path("<int:todo_id>/delete/", views.delete_todo, name="delete_todo"),
    path("<int:todo_id>/edit/", views.edit_todo, name="edit_todo"),
]
