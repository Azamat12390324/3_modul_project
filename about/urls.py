from django.urls import path
from about import views

app_name = 'about'


urlpatterns = [
    path('about_us', views.about_us, name='about_us'),
]