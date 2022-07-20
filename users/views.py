from django.shortcuts import render


"""
Many thanks to Chris Zielinski and CI's 'Boutique Ado'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/boutique_ado_v1
"""


def profile(request):
    """ Display the user's profile. """

    template = 'users/profile.html'
    context = {}

    return render(request, template, context)
