from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_todo_lists, name="my_todo_lists"),
    path("<int:task_id>/delete/", views.delete_task, name="delete_task"),
    path("<int:task_id>/edit/", views.edit_task, name="edit_task"),
]
