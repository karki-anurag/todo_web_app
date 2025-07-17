from django.db import models
from django.contrib.auth.models import User


class UserTodo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=[("low", "Low"), ("medium", "Medium"), ("high", "High")], default='medium')

def __str__(self):
    return f"{self.user.username} - {self.text[:10]}"
