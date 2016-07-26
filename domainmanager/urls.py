from django.conf import settings
from django.conf.urls import url
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

    # Create / Create one charactersheet
    #  ex: /domainmanager/character_create
    url(r'^character_create/', views.character_create, name='character_create'),

    # Create / Edit one charactersheet
    #  ex: /domainmanager/characterinformation/1/edit
    url(r'^characterinformation/(?P<character_id>[0-9]+)/edit/', views.characterinformation_edit, name='characterinformation_edit'),

    # Create / Edit one character's properties
    #  ex: /domainmanager/characterproperties/1/edit
    url(r'^characterproperties/(?P<character_id>[0-9]+)/edit/', views.characterproperties_edit, name='characterproperties_edit'),

    # List of all players
    #  ex: /domainmanager/players
    url(r'^players$', views.players, name='players'),

    # List all the characters
    # ex: /domainmanager/playersummary/1
    url(r'^playersummary/(?P<player_id>[0-9]+)$', views.playersummary, name='playersummary'),

    # View of the genealogy
    #  ex: /domainmanager/genealogy
    url(r'^genealogy$', views.genealogy, name='genealogy'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
