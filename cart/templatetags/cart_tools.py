from django import template

"""
Many thanks to Chris Zielinski and CI's 'Boutique Ado'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/boutique_ado_v1
"""


register = template.Library()


# decorator to register func as template filter
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
