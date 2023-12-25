from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n  import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_1.urls', namespace='default_1')),
    path('', include('home_2.urls')),
    path('',include('shop_layouts.urls')),
    path('',include('other_pages.urls')),
    path('',include('product_types.urls')), 
]

urlpatterns += i18n_patterns(
    path('', include('home_1.urls')),
) 
    




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
