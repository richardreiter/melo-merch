from django.shortcuts import render, redirect, reverse
from .forms import SubscribersForm, MailMessageForm
from .models import Subscribers
from django.contrib import messages
from django.core.mail import send_mail


"""
Many thanks to Kenneth Broni for a
great reference, inspiration and example:
https://www.youtube.com/watch?v=hWtlskOaFNI
"""
# Create your views here.


def newsletter(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription successful!')
            return redirect(reverse('newsletter'))
    else:
        form = SubscribersForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/newsletter.html', context)

