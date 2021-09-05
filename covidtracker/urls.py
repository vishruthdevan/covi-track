from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'covidtracker'

urlpatterns = [
    path('', views.index, name="index"),
]