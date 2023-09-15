from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def my_todo_lists(request):
    # Retrieve all instances of YourModel created by the currently logged-in user
    tasks_list = Task.objects.filter(created_by=request.user).order_by("date")
    taskform = TaskForm()

    if request.method == "POST":
        taskform = TaskForm(request.POST)
        if taskform.is_valid():
            new_record = taskform.save(commit=False)
            new_record.created_by = request.user  # Set the user
            new_record.save()
            return redirect("my_todo_lists")

    for record in tasks_list:
        if record.date < date.today():
            record.date = "ASAP!"

        elif record.date == date.today():
            record.date = "Today"

        elif (record.date - date.today()).days < 7:
            record.date = record.date.strftime("%A")

    context = {"records": tasks_list, "taskform": taskform}

    return render(request, "todolist/lists.html", context)


def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == "POST":
        taskform = TaskForm(request.POST, instance=task)
        if taskform.is_valid():
            taskform.save()
            return redirect("my_todo_lists")
    else:
        taskform = TaskForm(instance=task)

    return render(
        request, "todolist/edit_task.html", {"taskform": taskform, "record": task}
    )


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == "POST":
        task.delete()
        return redirect("my_todo_lists")

    return render(request, "todolist/delete_task.html", {"record": task})
