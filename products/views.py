from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
# object to generate search query
from django.db.models import Q
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
    # to avoid error when loading products page without search
    query = None

    if request.GET:
        # if text input q
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            # case insensitive and name or description 
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            # filter method to filter products
            products = products.filter(queries)

    # products to be available in template
    context = {
        'products': products,
        'search_term': query,
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
