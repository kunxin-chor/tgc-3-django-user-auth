
from django.contrib import admin
from django.urls import path, include
from .views import create_item

urlpatterns = [
    path('create', create_item, name='create_item')
]
