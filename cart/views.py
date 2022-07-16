from django.shortcuts import render, redirect

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



def add_to_cart(request, item_id):
    """
    Add a quantity of the specified
    product to the shopping cart
    """
    # get quantity from from
    quantity = int(request.POST.get('quantity'))
    # get redirect from form when process finished
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
