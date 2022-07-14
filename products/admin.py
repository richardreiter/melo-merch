from django.contrib import admin
# import product and category models
from .models import Product, Category

"""
Many thanks to Chris Zielinski and CI's 'Boutique Ado'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/boutique_ado_v1
"""
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    # fields to display within admin dash
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
    # sort products by sku
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    # fields to display within admin dash
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
