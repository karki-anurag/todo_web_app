from django.db import models
from django.contrib.auth.models import AbstractUser


#always migarte after creating or modifying models
# python manage.py makemigrations
# python manage.py migrate
class User(AbstractUser):
    gender = models.CharField(max_length=10, choices=[("male", "Male"), ("female", "Female"), ("other", "Other")], default="other")
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True) 
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(max_length=500, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True) # Fix upload_to path


    def __str__(self):
        return self.username
    
class Todo(models.Model):
    todo_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    task_name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=[("low", "Low"), ("medium", "Medium"), ("high", "High")], default='medium')
    image_url = models.ImageField(upload_to='todo_images/', null=True, blank=True) 

    def __str__(self):
        return self.task_name 
