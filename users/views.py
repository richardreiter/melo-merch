from django.shortcuts import render, get_object_or_404

from .models import UserProfile


"""
Many thanks to Chris Zielinski and CI's 'Boutique Ado'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/boutique_ado_v1
"""


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'users/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
