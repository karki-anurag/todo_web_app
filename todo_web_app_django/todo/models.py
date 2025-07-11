from django.db import models


class users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    gender =models.CharField(max_length=10, choices=[("male", "Male"),("female", "Female"),("other", "Other")], default='Other')
    phone_number = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(max_length=500)
    profile_picture = models.ImageField(upload_to= 'profile_picture/', null=True, blank=True)

    def __str__(self):
        return self.username
    
class Todo(models.Model):
    todo_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(users, on_delete=models.CASCADE, related_name='todos')
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
