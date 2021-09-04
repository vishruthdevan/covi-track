from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
]