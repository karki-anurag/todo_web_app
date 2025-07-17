Learnings:
# Context Variables: These are the variable tha helps us to pass the views data in templates.
# REQUIRED_FIELS  :  These are that extra fields that are necessary   to have when creating a  super user.

# AuthitactionForm: This is the special kind of form that helps the admin to outsource valadating a user. i.e it provides differet authincation features by itself. path: django.contrib.auth.forms import authincationform

#  User Creation form: this form has predefined fields for the user and you can also add your custon fields.

# Difference between forms.Forms and AuthintacationForms: forms.Forms is like blank paper where you can have any fields according to your needs, but In AuthinticationForms, you would have some predefined fields.


# Authentication and session flow in Django:-  when user got loged in to our website. i login view we redirect the user to task list and then we use is_authinticated feature to ensure that this is the correct user using a decorater i.e@login_required, between them i.e login view and task_list view, a session got established for a limited amount of time which is provided by djangomiddlarewares which provides us a ticket to identify the user and fetch the data based on the user.

# inheriated Form should use meta class to custon inject the fields and should have to specify the model from which the fields should come.

# 'WSGIRequest' object has no attribute 'get': this error comes when youre "method" or "post" spelling are wrong

# .filter()
This is the method that helps us to retrive the data if the method matches provided conditions.