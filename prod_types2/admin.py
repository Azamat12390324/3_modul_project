from django.contrib import admin
from prod_types2.models import Tab_left, Gallery_left, Sticky_left



@admin.register(Tab_left)
class Tab_left(admin.ModelAdmin):
    list_display = ('title', 'sub_title', )
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)

@admin.register(Gallery_left)
class Gallery_left(admin.ModelAdmin):
    list_display = ('title', 'sub_title', )
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)

@admin.register(Sticky_left)
class Sticky_left(admin.ModelAdmin):
    list_display = ('title', 'sub_title', )
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)

