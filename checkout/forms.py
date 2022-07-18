from django import forms
from .models import Order

"""
Many thanks to Chris Zielinski and CI's 'Boutique Ado'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/boutique_ado_v1
"""


class OrderForm(forms.ModelForm):
    class Meta:
        # associated model
        model = Order
        # fields to render
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        # override init method to customise
        super().__init__(*args, **kwargs)
        # dict of placeholders to show in form fields
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        # cursor starts in full_name when page loads
        self.fields['full_name'].widget.attrs['autofocus'] = True
        # iterate through fields
        for field in self.fields:
            # add * if field required
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            # set attr to their values in dict
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # add css class
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # remove fields labels
            self.fields[field].label = False
