from django.urls import path
from blog import views

app_name = 'blog'


urlpatterns = [
    path('grid_sidebar', views.grid_sidebar, name='grid_sidebar'),
    path('full_width',views.full_width, name='full_width'),
    path('single_sidebar',views.single_sidebar, name='single_sidebar'), 
]