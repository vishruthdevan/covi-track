from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('register-info/', views.Info.as_view(), name='register_info'),
]