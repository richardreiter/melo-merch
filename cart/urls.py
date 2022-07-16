from django.urls import path
from . import views


"""
Many thanks to Chris Zielinski and CI's 'Boutique Ado'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/boutique_ado_v1
"""


urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add(<item_id>/', views.add_to_cart, name='add_to_cart'),
]
