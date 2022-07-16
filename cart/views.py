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
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    # if a product with size is being added
    if size:
        # if the item is already in the cart
        if item_id in list(cart.keys()):
            # check if another item of same id and size is in cart
            if size in cart[item_id]['items_by_size'].keys():
                # if so increment quantity for that size
                cart[item_id]['items_by_size'][size] += quantity
            # otherwise set it equal to the quantity
            else:
                cart[item_id]['items_by_size'][size] = quantity
        # add to cart if not there
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
