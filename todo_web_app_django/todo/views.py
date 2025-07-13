from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, RegistrationForm
from .models import User
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    # This is a simple view that returns a response
    users = User.objects.all()
    return render(request, 'home.html', {'users': users})

def tasks_list(request):
    # This is a simple view that returns a response
    return render(request, 'tasks_list.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            pass
    else:
        form = RegistrationForm(request.POST)      
    return render(request, 'register.html', {'form': form})



def login(request):
    # This is a simple view that returns a response
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                # User is authenticated, redirect to home or dashboard
                messages.success(request, "Login successful")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password")
                return redirect('login')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

def about_us(request):
    # This is a simple view that returns a response
    return render(request, 'about_us.html')

def profile(request):
    # This is a simple view that returns a response
    return render(request, 'profile.html')