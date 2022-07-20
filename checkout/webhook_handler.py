from django.http import HttpResponse


"""
Many thanks to Chris Zielinski and CI's 'Boutique Ado'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/boutique_ado_v1
"""


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
