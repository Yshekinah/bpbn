from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^domainmanager/', include('domainmanager.urls')),
    url(r'^admin/', admin.site.urls),
]
