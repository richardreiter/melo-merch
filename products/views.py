from django.shortcuts import render
from .models import Product

# Create your views here.
"""
Many thanks to Chris Zielinski and CI's 'Boutique Ado'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/boutique_ado_v1
"""


def all_products(request):
    """
    A view to show all products,
    including sorting and search queries
    """

    # return products from db
    products = Product.objects.all()

    # products to be available in template
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
