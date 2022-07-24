from django.shortcuts import render, redirect, reverse
from .forms import SubscribersForm, MailMessageForm
from .models import Subscribers
from django.contrib import messages


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


def mail_letter(request):
    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been \
                successfully sent to the Mailing list!')
            return redirect(reverse('mail_letter'))
    else:
        form = MailMessageForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/mail_letter.html', context)
