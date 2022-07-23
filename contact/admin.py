from django.contrib import admin
from .models import Contact

# Register your models here.


class ContactFormAdmin(admin.ModelAdmin):
    """
    Register contact form
    in admin panel
    """

    list_display = (
        'name',
        'email',
        'subject',
        'message',
    )
    # order by created on date
    ordering = ('created_on',)


admin.site.register(Contact, ContactFormAdmin)