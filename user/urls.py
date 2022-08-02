from django.urls import path
from .api import create_user, get_user

urlpatterns = [
    # POST Requests
    path('post/user/signup', create_user),
    path('post/user/login', get_user)
]