# todo_web_app_django/todo/urls.py
# URL configuration for the todo app.
from django.urls import path
from todo import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/login/lists/', views.lists, name='lists'),
    path('accounts/login/create/', views.create, name='create'),
    path('about_us/', views.about_us, name='about_us'),
    path('profile/', views.profile, name='profile'),
]
