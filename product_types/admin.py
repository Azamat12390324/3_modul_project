from django.contrib import admin
from product_types.models import Default, Variable,  Referral, Group, Slider



@admin.register(Default)
class Default(admin.ModelAdmin):
    list_display = ('title', 'sub_title', )
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)

@admin.register(Variable)
class Variable(admin.ModelAdmin):
    list_display = ('title', 'sub_title', )
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)

@admin.register(Referral)
class Referral(admin.ModelAdmin):
    list_display = ('title', 'sub_title', )
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)

@admin.register(Group)
class Group(admin.ModelAdmin):
    list_display = ('title', 'sub_title', )
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)

@admin.register(Slider)
class Slider(admin.ModelAdmin):
    list_display = ('title', 'sub_title', )
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)

