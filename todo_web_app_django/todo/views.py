
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # This is a simple view that returns a response
    return render(request, 'home.html', )

def task_list(request):
    # This is a simple view that returns a response
    return render(request, 'task_list.html')

def register(request):
    # This is a simple view that returns a response
    return HttpResponse("This is the registration page.")

def login(request):
    # This is a simple view that returns a response
    return HttpResponse("This is the login page.")