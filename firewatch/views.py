# filepath: /c:/Users/muham/OneDrive/Documents/FrlanceWork/afnanproject/mainproject/firewatch/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import PreviewImage
from .models import ImageUpload
import os

BASE_DIR = os.path.curdir
BASE_DIR.join("/media/images")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("Username")
        password = request.POST.get("Password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("Username")
        password = request.POST.get("Password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return render(request, "register.html")

        user = User.objects.create_user(username=username, password=password)
        user.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect("login")

    return render(request, "register.html")

@login_required(login_url="login")
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect('login')

@login_required(login_url="login")
def index(request):
    return render(request, "index.html")

@login_required(login_url="login")
def live(request):
    return render(request, "live.html")

@login_required(login_url="login")
def preview(request):
    user = request.user
    if request.method == "POST":
        form = PreviewImage(request.POST, request.FILES)
        if form.is_valid():
            image_upload = form.save(commit=False)
            image_upload.user = user
            image_upload.save()
            return redirect("live")
    else:
        form = PreviewImage()

    return render(request, "upload.html", {"form": form})