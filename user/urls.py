from django.urls import path
from .views import lists, registration, user_profile, create, mark, edit, delete


urlpatterns = [
    path('lists/',lists,name = 'lists' ),
    path('create/',create,name = 'create' ),
    path('register/',registration,name='register'),
    path('userprofile/',user_profile,name='userprofile'),
    path('lists/<int:id>/', mark, name='mark'),
    path('lists/<int:id>/edit', edit, name='edit'),
    path('lists/<int:id>/delete', delete, name='delete'),



]