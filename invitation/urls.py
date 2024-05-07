from django.contrib import admin
from django.urls import path, include
from .views import index, nudes

urlpatterns = [
  
    path('', index),
    path('nudes/', nudes),
]
