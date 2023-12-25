from django.contrib import admin
from other_pages.models import Cart, Wishlist, Compare, Checkout, Login, Account


@admin.register(Cart)
class Cart(admin.ModelAdmin):
    list_display = ('title', 'sub_title', )
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)

@admin.register(Wishlist)
class Wishist(admin.ModelAdmin):
    list_display = ('title', 'sub_title', )
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)

@admin.register(Compare)
class Compare(admin.ModelAdmin):
    list_display = ('title', 'sub_title', )
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)

@admin.register(Checkout)
class Checkout(admin.ModelAdmin):
    list_display = ('title', 'sub_title', )
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)

@admin.register(Login)
class Login(admin.ModelAdmin):
    list_display = ('title', 'sub_title', )
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)

@admin.register(Account)
class Account(admin.ModelAdmin):
    list_display = ('title', 'sub_title', )
    list_display_links = ('title', 'sub_title')
    list_filter = ('title',)




