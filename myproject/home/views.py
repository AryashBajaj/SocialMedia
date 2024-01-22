from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request) :
    context = {
        "variable" : "This is sent",
    }
    return render(request, "index.html", context)

def about(request) :
    return HttpResponse("This is about page.")

def services(request) :
    return HttpResponse("This is services page.")

def contact(request) :
    if request.method == "POST" :
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = Contact(name=name, email=email, password=password, date=datetime.today())
        contact.save()

    return render(request, "contact.html")

