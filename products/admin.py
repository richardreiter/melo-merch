from django.contrib import admin
# import product and category models
from .models import Product, Category

"""
Many thanks to Chris Zielinski and CI's 'Boutique Ado'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/boutique_ado_v1
"""
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
