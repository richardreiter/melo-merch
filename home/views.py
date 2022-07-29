from django.shortcuts import render

# Create your views here.


"""
Many thanks to Chris Zielinski and CI's 'Boutique Ado'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/boutique_ado_v1
"""


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def faq(request):
    """ A view to return the faq page """

    return render(request, 'home/faq.html')
