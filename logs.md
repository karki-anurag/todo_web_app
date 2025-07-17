# First Error:-
# Home.html File not found by the Django panal.
# Steps Taken:- 
1) Settings.py file, i have configured templates.
2) I have checked the names of the files. They are alos matching.
3) templates folder is inside the root directory of todo_web_app.
4) Onto root urls.py, I have correctly configured ('', TemplateView.as_view(template_name = home), name = 'home')
# Error Solved

# Second Error:- when i am trying to go to login page. it is automatically being fordwarded to accounts/login because i have used @login_required decorator.
# The link i am getting fordwarded to is account/login
# Solution:- i have manually configured my login into accounts/login

# Third Error:- 'WSGIRequest' object has no attribute 'get'
Thoughts:- This error can occurs due to differents things. Some of them are:-
1) when the spelling of 'method' or  'post' is wrong.
2) The second error is trying to pass the whole request into where it should not have the access. i.e form = TodoForm(request.FILES, request.POST), this only accepts the request.get() , request.post short of paramete and when we try to pass the whole request such errors occurs.
# There is an exception, loginform need to have the whole request because it manages sessionstime, user ip address, any type of dat available on the browser.
# Solved


# Fourth Error:- In case of data is not passing in templates through views.
# If we are already creating a dictionary that holds the user data. we have to either pass value of the dictionry as a context variable or we have to pass the entire vaiable as the Context variable.