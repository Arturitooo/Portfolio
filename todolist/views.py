from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todos
from .forms import TodosForm
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def my_todos(request):
    # Retrieve all instances of YourModel created by the currently logged-in user
    todos_list = Todos.objects.filter(created_by=request.user).order_by("date")
    form = TodosForm()

    if request.method == "POST":
        form = TodosForm(request.POST)
        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.created_by = request.user  # Set the user
            new_record.save()
            return redirect("my_todos_list")

    for record in todos_list:
        the_date = record.date
        if the_date == date.today():
            record.date = "Today"
        elif (the_date - date.today()).days < 7:
            record.date = the_date.strftime("%A")

    context = {"records": todos_list, "form": form}

    return render(request, "todolist/list.html", context)


def edit_todo(request, todo_id):
    todo = get_object_or_404(Todos, pk=todo_id)

    if request.method == "POST":
        form = TodosForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("my_todos_list")
    else:
        form = TodosForm(instance=todo)

    return render(request, "todolist/edit_todo.html", {"form": form, "record": todo})


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todos, pk=todo_id)

    if request.method == "POST":
        todo.delete()
        return redirect("my_todos_list")

    return render(request, "todolist/todo_delete.html", {"record": todo})
