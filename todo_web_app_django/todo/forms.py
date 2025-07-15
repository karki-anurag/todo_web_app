from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . models import User, Todo

class RegistrationForm(UserCreationForm):
    class Meta:
        model =  User 
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'gender',
            'phone_number',
            'date_of_birth',
            'address',
            'profile_picture'
        )
        # You can add widgets here for custom HTML attributes
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'e.g., +977-98XXXXXXXX'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}), # HTML5 date picker
            'address': forms.Textarea(attrs={'rows': 4}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Your Password'}))

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = (
            'task_name',
            'description',
            'due_date', 
            'priority', 
            'image_url'
        )
        widgets = {
            'due_date' : forms.DateInput(attrs={'type': 'date'})
        }

        
        

