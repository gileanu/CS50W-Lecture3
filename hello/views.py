from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def gileanu(request):
    return HttpResponse("Hello gileanu!")

def david(requet):
    return HttpResponse("Hello David!")

def greet(request, name):
    return render(request, "hello/great.html", {
        "name": name.capitalize()
    })