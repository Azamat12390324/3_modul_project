from django.contrib import admin
from shop_layouts.models import Grid_Left , Full_width , List_sidebar


@admin.register(Grid_Left)
class Grit_left(admin.ModelAdmin):
    list_display = ('title', 'sub_title', )
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)

@admin.register(Full_width)
class Full_width(admin.ModelAdmin):
    list_display = ('title', 'sub_title', )
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)

@admin.register(List_sidebar)
class List_sidebar(admin.ModelAdmin):
    list_display = ('title', 'sub_title', )
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)


