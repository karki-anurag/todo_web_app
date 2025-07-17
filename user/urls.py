from django.urls import path
from .views import lists, registration,user_profile,create


urlpatterns = [
    path('lists/',lists,name = 'lists' ),
    path('create/',create,name = 'create' ),
    path('register/',registration,name='register'),
    path('userprofile/',user_profile,name='userprofile'),
]