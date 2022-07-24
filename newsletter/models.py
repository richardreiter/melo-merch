from django.db import models

# Create your models here.
"""
Many thanks to Kenneth Broni for a
great reference, inspiration and example:
https://www.youtube.com/watch?v=hWtlskOaFNI
"""


class Subscribers(models.Model):
    """
    Record the subscribers form
    to database
    """
    class Meta:  # adjust plural form
            verbose_name_plural = 'Subscribers'
        
    # subscriber's email
    email = models.EmailField(max_length=254, null=True)
    # date subscribed
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class MailMessage(models.Model):
    # message title
    title = models.CharField(max_length=120, null=True)
    # message
    message = models.TextField(null=True)

    def __str__(self):
        return self.title
