from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from main.forms import RegisterForm

# Create your views here.
def home(request) :
    return render(request, "main/home.html")

def sign_up(request) :
    if request.method == "POST" :
        form = RegisterForm(request.POST)
        if form.is_valid() :
            user = form.save()
            login(request, user)
            return redirect('/home')
    else :
        form = RegisterForm()
    return render(request, "registration/sign_up.html", {"form" : form})