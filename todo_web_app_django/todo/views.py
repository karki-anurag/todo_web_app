
from django.shortcuts import redirect, render
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate 

# Create your views here.
def home(request):
    # This is a simple view that returns a response
    return render(request, 'home.html', )

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
        form = LoginForm(request.POST)
        if form.is_valid():
            # Here you would typically authenticate the user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # User is authenticated, redirect to home
                return redirect('home')
            else:
                # Invalid credentials, handle accordingly
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})