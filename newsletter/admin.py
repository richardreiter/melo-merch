from django.contrib import admin
from . models import MailMessage, Subscribers


"""
Many thanks to Kenneth Broni for a
great reference, inspiration and example:
https://www.youtube.com/watch?v=hWtlskOaFNI
"""
# Register your models here.
admin.site.register(MailMessage)
admin.site.register(Subscribers)
