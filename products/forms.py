from django import forms
from .models import Product, Category

"""
Many thanks to Chris Zielinski and CI's 'Boutique Ado'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/boutique_ado_v1
"""


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        # include all the fields
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # override method
        super().__init__(*args, **kwargs)
        # get all categories
        categories = Category.objects.all()
        # create a list of tuples of friendly names
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # update category fields on the form with friendly names
        self.fields['category'].choices = friendly_names
        # iterate thru rest of fields and apply classes
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
