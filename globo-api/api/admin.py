"""Admin for Inquiry"""
from django.contrib import admin

from .models import Inquiry

class InquiryAdmin(admin.ModelAdmin):
    """Inquiry Admin"""
    list_display = (
        'name',
        'email',
        'remarks',
    )

admin.site.register(Inquiry, InquiryAdmin)

# Register your models here.
