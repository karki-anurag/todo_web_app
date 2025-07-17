from django.shortcuts import redirect, render, get_object_or_404
from .models import UserTodo
from .forms import TodoForm, RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def lists(request):
    tasks = UserTodo.objects.all()
    return render(request, 'lists.html', {'tasks': tasks})

@login_required
def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            messages.success(request, "Successfully Created")
            return redirect('lists') # we are not redirecting to 'list' on the basis of ouur html. we are doing it on the basis of 'lisr view'
    else:
        form = TodoForm()
    return render(request, 'create.html', {'form': form})

def edit(request, task_id):
  tasks = get_object_or_404(UserTodo, pk = task_id, user = request.user)
  if request.method == 'POST':
    form = TodoForm(request.POST, instance = tasks)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
  else:
       form = TodoForm(instance = tasks ) #we use instance to provide prefill data to the user which is comming from model 'UserTodo'
  return render(request, 'create.html', {'form': form})  

@login_required
def tweet_delete(request, task_id):
    tasks = get_object_or_404(UserTodo, pk = task_id, user = request.user)
    if request.method == 'POST':
        tasks.delete()
        return redirect('tweet_list')
    return render(request, 'task_confirm_delete.html', {'tasks': tasks})

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('lists')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_profile(request):
    return render(request, 'userprofile.html')