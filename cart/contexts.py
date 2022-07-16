from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

"""
Many thanks to Chris Zielinski and CI's 'Boutique Ado'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/boutique_ado_v1
"""


# context processor
def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    # create an empty library if there are no items in the cart
    cart = request.session.get('cart', {})

    # for each item id and quantity in cart items
    for item_id, quantity in cart.items():
        # get product
        product = get_object_or_404(Product, pk=item_id)
        # add its quantity times the total price
        total += quantity * product.price
        # increment count by quantity
        product_count += quantity
        # add dict to cart list
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    # delivery logic
    if total < settings.FREE_DELIVERY_THRESHOLDS:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        # how much user needs to spend to get free delivery
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLDS - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    # items to be available in templates across site
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLDS,
        'grand_total': grand_total,
    }

    return context
