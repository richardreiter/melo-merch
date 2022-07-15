from django.shortcuts import render

# Create your views here.
"""
Many thanks to Chris Zielinski and CI's 'Boutique Ado'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/boutique_ado_v1
"""


def view_cart(request):
    """
    A view to return the cart contents page
    """
    return render(request, 'cart/cart.html')
