from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

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


def adjust_cart(request, item_id):
    """
    Adjust the quantity of the specified product to the specified amount
    """
    # just in case product isn't found
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            # set items qty accordingly
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {cart[item_id]["items_by_size"][size]}')
        # otherwise remove item
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop[item_id]
            messages.success(request, f'Removed size {size.upper()} {product.name} from your cart')

    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """
    Remove the item from the cart
    """

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your cart')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        # item successfully removed
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        # return error message
        return HttpResponse(status=500)


def add_to_cart(request, item_id):
    """
    Add a quantity of the specified
    product to the shopping cart
    """
    # just in case product isn't found
    product = get_object_or_404(Product, pk=item_id)
    # get quantity
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
                # updated message for products with sizes
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {cart[item_id]["items_by_size"][size]}')
            # otherwise set it equal to the quantity
            else:
                cart[item_id]['items_by_size'][size] = quantity
                # message for adding an item with same size already in the bag
                messages.success(request, f'Added size {size.upper()} {product.name} to your cart')
        # add to cart if not there
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            # message added item with a size
            messages.success(request, f'Added size {size.upper()} {product.name} to your cart')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            # message user updated quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart[item_id] = quantity
            # let user know they've added product to cart
            messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)
