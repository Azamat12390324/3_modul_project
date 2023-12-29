from django.contrib import admin
from blog.models import  Grid_sidebar, Full_width, Single_sidebar

@admin.register(Grid_sidebar)
class Grid_sidebar(admin.ModelAdmin):
    list_display = ('title', 'sub_title', )
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)

@admin.register(Full_width)
class Full_width(admin.ModelAdmin):
    list_display = ('title', 'sub_title', )
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)

@admin.register(Single_sidebar)
class Single_sidebar(admin.ModelAdmin):
    list_display = ('title', 'sub_title', )
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)



