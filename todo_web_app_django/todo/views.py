from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, RegistrationForm,TodoForm
from .models import Todo
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            next_url = request.GET.get('next') or 'home'
            return redirect(next_url)
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
                next_url = request.GET.get('next') or 'create'
                return redirect(next_url)
            else:
                messages.error(request, "Invalid username or password")
                return render(request, 'login.html', {'form':form})
        else:
            messages.error(request, "The Data you sumitted is not Valid!")
            return render(request, 'login.html', {'form':form})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

@login_required
def lists(request):
    # This is a simple view that returns a the task that user has created.
    user_todo = Todo.objects.filter(user = request.user)
    tasks = {
        'tasks': user_todo,
    }
    
    return render(request, 'lists.html',tasks)

@login_required
def create(request):
    if request.method == 'POST':
        form = TodoForm( request.POST, request.FILES)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            messages.success(request, "Task created successfully!")
            return redirect('lists')
        else:  
            messages.error(request, "Please correct the errors in the form.")
            return render(request, 'create.html', {'form': form})
    else:
        form = TodoForm()
    return render(request, 'create.html', {'form': form})



def about_us(request):
    # This is a simple view that returns a response
    return render(request, 'about_us.html')

def profile(request):
    # This is a simple view that returns a response
    return render(request, 'profile.html')