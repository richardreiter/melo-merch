from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
"""
Many thanks to Chris Zielinski and CI's 'Boutique Ado'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/boutique_ado_v1
"""


def all_products(request):
    """
    View to show all products,
    including sorting and search queries
    """

    # return products from db
    products = Product.objects.all()

    # products to be available in template
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    View to show individual product details
    """
    # take product id as a param
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    # return template including product
    return render(request, 'products/product_detail.html', context)
