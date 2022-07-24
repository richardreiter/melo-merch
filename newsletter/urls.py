from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.newsletter, name='newsletter'),
    path('mail_letter/', views.mail_letter, name='mail_letter'),
]
