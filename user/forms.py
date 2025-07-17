from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserTodo
from django.contrib.auth.models  import User

class TodoForm(forms.ModelForm):
    class Meta:
        model = UserTodo
        fields = [
            'task_name',
            'description',
            'priority'
        ]

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')