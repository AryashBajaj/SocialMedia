from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user

# Create your views here.
def index(request) :
    if get_user(request).is_anonymous :
        redirect("/login/", permanent=True)
    else :
        messages.success(request, "Logged in!")
    context = {
        "variable" : "This is sent",
    }
    return render(request, "index.html", context)

def about(request) :
    return HttpResponse("This is about page.")

def services(request) :
    return HttpResponse("This is services page.")

def loginUser(request) :
    if request.method == "POST" :
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None :
            messages.success(request, "Succesfully logged in!")
            login(request, user)
            redirect("index.html", permanent=True)
        else :
            messages.error(request, "Could not login, please re-check the entered credentials.")
    return render(request, "login.html")

def logoutUser(request) :
    if request.method == "POST" :
        logout(request)
        messages.success(request, "Logged out succesfully!")
        redirect('login.html')
    return HttpResponse("Logged out!")
    

def contact(request) :
    if request.method == "POST" :
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = Contact(name=name, email=email, password=password, date=datetime.today())
        contact.save()
        messages.success(request, 'Profile details updated!')

    return render(request, "contact.html")



