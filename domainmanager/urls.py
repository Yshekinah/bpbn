from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'domainmanager'

urlpatterns = [
    # ex: /domainmanager/
    url(r'^$', views.index, name='index'),

    # List of all characters
    #  ex: /domainmanager/characters
    url(r'^characters$', views.characters, name='characters'),

    # View one charactersheet
    #  ex: /domainmanager/charactersheet/1
    url(r'^charactersheet/(?P<character_id>[0-9]+)$', views.charactersheet, name='charactersheet'),

    # List of all players
    #  ex: /domainmanager/players
    url(r'^players$', views.players, name='players'),

    # List all the characters
    # ex: /domainmanager/playersummary/1
    url(r'^playersummary/(?P<player_id>[0-9]+)$', views.playersummary, name='playersummary'),

    # View of the genealogy
    #  ex: /domainmanager/genealogy
    url(r'^genealogy/', views.genealogy, name='genealogy'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
