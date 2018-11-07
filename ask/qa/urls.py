from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<id>/', views.question, name='question'),
]
