from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegisterForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("booking")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("booking")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "users/login.html")

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("main:home")
