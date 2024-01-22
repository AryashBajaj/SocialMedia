from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request) :
    return render(request, "index.html")

def about(request) :
    return HttpResponse("This is about page.")

def services(request) :
    return HttpResponse("This is services page.")
