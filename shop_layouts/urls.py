from django.urls import path
from shop_layouts import views

app_name = 'shop_layouts'


urlpatterns = [
    path('', views.grid_left, name='grid_left'),
    path('full_with',views.full_width, name='full_width'),
    path('list_sidebar',views.list_sidebar, name='list_sidebar'),    
]
