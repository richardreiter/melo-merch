from django.contrib import admin
from django.urls import path
from . import views


"""
Many thanks to Chris Zielinski and CI's 'Boutique Ado'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/boutique_ado_v1
"""


urlpatterns = [
    # root url render index named home
    path('', views.index, name='home'),
    path('faq/', views.faq, name='faq'),
    path('about/', views.about, name='about'),
]
