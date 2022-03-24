from unicodedata import name
from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'^$', user_list, name='user_list'),
    path('login_attempts', login_attempts, name='login_attempts'),
    path('register_attempts', register_attempts, name='register_attempts'),
    path("logout_attempts", logout_attempts, name='logout_attempts'),
]
