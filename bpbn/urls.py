from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^domainmanager/', include('domainmanager.urls')),
#    url(r'^grappelli/', include('grappelli.urls')), # for clean backend editor
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
