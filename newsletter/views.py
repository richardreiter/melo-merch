from django.shortcuts import render, redirect, reverse
from .forms import SubscribersForm, MailMessageForm
from .models import Subscribers
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame


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
    # get all subs emails
    emails = Subscribers.objects.all()
    # put in a data frame
    df = read_frame(emails, fieldnames=['email'])
    # turn values into a list
    mail_list = df['email'].values.tolist()
    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            # send email with form details
            send_mail(
                title,  # title
                message,  # message
                '',
                mail_list,  # subs email list
                # to avoid breaking if an email bounces back
                fail_silently=False,
            )
            messages.success(request, 'Your message has been \
                successfully sent to the Mailing list!')
            return redirect(reverse('mail_letter'))
    else:
        form = MailMessageForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/mail_letter.html', context)
