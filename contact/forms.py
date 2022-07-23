from django import forms


class ContactForm(forms.Form):
    """
    A contact form for users
    to ask questions and  provide feedback
    to shop owner
    """
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(widget=forms.EmailInput(), label='Email Address')
    subject = forms.CharField(label='Subject', max_length=120)
    message = forms.CharField(label='Message', max_length=900, widget=forms.Textarea())
