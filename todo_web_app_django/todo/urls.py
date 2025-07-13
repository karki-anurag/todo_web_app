# todo_web_app_django/todo/urls.py
# URL configuration for the todo app.
from django.urls import path
from todo import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks_list/', views.tasks_list, name='tasks_list'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]
