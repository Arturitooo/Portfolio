from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.


def mainpage(request):
    return render(request, "general/index.html")


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, log the user in after registration
            # auth.login(request, user)
            return redirect(
                "login"
            )  # Redirect to the login page after successful registration
    else:
        form = CustomUserCreationForm()

    return render(request, "general/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a page after successful login (e.g., 'home')
            return redirect("mainpage")
        else:
            messages.error(request, "username or password not correct")
            return redirect("login")

    return render(request, "general/login.html")


def user_logout(request):
    logout(request)
    # Redirect to a page after successful logout (e.g., 'home')
    return redirect("mainpage")
