from django.contrib import admin
from contact.models import  Contact_us

@admin.register(Contact_us)
class Contact_us(admin.ModelAdmin):
    list_display = ('title', 'sub_title', )
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)


