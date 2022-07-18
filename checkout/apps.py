from django.apps import AppConfig

"""
Many thanks to Chris Zielinski and CI's 'Boutique Ado'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/boutique_ado_v1
"""


class CheckoutConfig(AppConfig):
    name = 'checkout'

    # override ready method and import signals
    def ready(self):
        import checkout.signals
