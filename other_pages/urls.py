from django.urls import path
from other_pages import views

app_name = 'other_pages'


urlpatterns = [
    path('cart', views.cart, name='cart'),
    path('wishlist',views.wishlist, name='wishlist'),
    path('compare',views.compare, name='compare'), 
    path('checkout',views.checkout, name='checkout'),
    path('login',views.login, name='login'),
    path('account',views.account, name='account'),
      
]
