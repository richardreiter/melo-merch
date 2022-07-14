from django.urls import path
from . import views

"""
Many thanks to Chris Zielinski and CI's 'Boutique Ado'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/boutique_ado_v1
"""


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
]
