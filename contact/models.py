from django.db import models

# Create your models here.

class Contact(models.Model):
    """
    Record the contact form
    to database
    """

    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=120, null=False, blank=False)
    message = models.TextField(max_length=900, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + '___' + self.subject
