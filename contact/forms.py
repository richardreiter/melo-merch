from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    A contact form for users
    to ask questions and  provide feedback
    to shop owner
    """
    class Meta:
        model = Contact
        # include all the fields
        fields = '__all__'
