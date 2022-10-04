from django.urls import path
from . import views
from django.urls import re_path as url


urlpatterns = [
    url('', views.main_page, name='main'),
    url('register/', views.register, name='register')
]