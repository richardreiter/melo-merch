from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


"""
Many thanks to Chris Zielinski and CI's 'Boutique Ado'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/boutique_ado_v1
"""


def checkout(request):
    # get cart from session
    cart = request.session.get('cart', {})
    # if cart empty
    if not cart:
        # add error msg
        messages.error(request, "There's nothing in your cart at the moment")
        # redirect prod page
        return redirect(reverse('products'))

    # instance of order_form
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LNGE1Cf3qMNtRlhxGUCWybJO2ll4q5M91wD9lgjCDku4nR4jdR91FQrg9kWHJHn7tzD8ssGMJ5mCyEPDuFCOf5c00V4LJoMjg',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
