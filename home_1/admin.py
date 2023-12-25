from django.contrib import admin
from home_1.models import Home_1


@admin.register(Home_1)
class Home_1(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'icons')
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)


