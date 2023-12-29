from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n  import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_1.urls', namespace='default_1')),
    path('', include('home_2.urls', namespace='default_2')),
    path('',include('shop_layouts.urls')),
    path('',include('other_pages.urls')),
    path('',include('product_types.urls')), 
    path('',include('prod_types2.urls')),
    path('',include('blog.urls')),
    path('',include('pages.urls')),
    path('',include('about.urls')),
    path('',include('contact.urls'))
]

urlpatterns += i18n_patterns(
    path('', include('home_1.urls')),
    path('',include('home_2.urls')),
) 
    





if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
