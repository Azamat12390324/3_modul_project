from django.contrib import admin
from about.models import  About_us

@admin.register(About_us)
class About_us(admin.ModelAdmin):
    list_display = ('title', 'sub_title', )
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)


