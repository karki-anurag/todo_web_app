from django.contrib import admin
from .models import UserTodo

# Register your models here.


#we can customize how can we see the data


#we can link them by two methods: First_One: 
# first is the Model 
# that we have registered to the user and the second is The Admin class from where we can customize how we can see data
class UserTodoAdmin(admin.ModelAdmin):
    list_display = ['task_name','description', 'is_completed', 'user_id']
    list_filter = ['user_id']
admin.site.register(UserTodo, UserTodoAdmin)

#we can link them by two methods: Second_one: Using decoraters
#using:# @admin.register(UserTodo)

