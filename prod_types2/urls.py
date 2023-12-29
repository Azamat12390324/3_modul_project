from django.urls import path
from prod_types2 import views

app_name = 'prod_types2'


urlpatterns = [
    path('tab_left', views.tab_left, name='tab_left'),
    path('gallery_left',views.gallery_left, name='gallery_left'),
    path('sticky_left',views.sticky_left, name='sticky_left'), 
]