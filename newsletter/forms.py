from django import forms
from .models import Subscribers, MailMessage


class SubscribersForm(forms.ModelForm):
    """
    A contact form for users
    to provide their email
    address to subscribe
    to the shop's newsletter
    """
    class Meta:
        model = Subscribers
        fields = ['email', ]


class MailMessageForm(forms.ModelForm):
    """
    A form for the
    shop owner to send
    newsletters to the shoppers
    """
    class Meta:
        model = MailMessage
        # include all the fields
        fields = '__all__'
