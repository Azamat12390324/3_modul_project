from django.urls import path
from product_types import views

app_name = 'product_types'


urlpatterns = [
    path('default', views.default, name='default'),
    path('variable',views.variable, name='variable'),
    path('referral',views.referral, name='referral'), 
    path('group',views.group, name='group'),
    path('slider',views.slider, name='slider'),

      
]