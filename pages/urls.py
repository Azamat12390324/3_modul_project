from django.urls import path
from pages import views

app_name = 'pages'


urlpatterns = [
    path('pages', views.servise, name='servise'),
    path('frequently',views.frequently, name='frequently'),
    path('privacy_policy',views.privacy_policy, name='privacy_policy'),
    path('page_404',views.page_404, name='page_404') 
]