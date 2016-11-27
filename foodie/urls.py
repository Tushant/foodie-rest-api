from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^restaurant/', include('restaurants.urls')),
    # url(r'^(?:.*)/?$', include('restaurants.urls')),
    url(r'^api/restaurant/', include('restaurants.api.urls')),
    url(r'^api/customer/', include('userprofiles.api.urls', namespace='customer')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/', include('allauth.urls')),
    # url(r'^order/', include('orders.urls')),
    # url(r'^review/', include('reviews.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
