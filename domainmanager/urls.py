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

    # View xp for one character
    #  ex: /domainmanager/characterxpsummary/1
    url(r'^characterxpsummary/(?P<character_id>[0-9]+)$', views.characterxpsummary, name='characterxpsummary'),

    # View boons for one character
    #  ex: /domainmanager/characterxpsummary/1
    url(r'^characterboonsummary/(?P<character_id>[0-9]+)$', views.characterboonsummary, name='characterboonsummary'),

    # View boons for one character
    #  ex: /domainmanager/characterxpsummary/1
    url(r'^characterboon_create/(?P<character_id>[0-9]+)/create$', views.characterboon_create, name='characterboon_create'),

    # Validate boons for one character
    #  ex: /domainmanager/characterboon_validation/1/1bfkdjbf/2
    url(r'^characterboon_validation/(?P<boon_id>[0-9]+)/(?P<hash>[A-Za-z0-9]+)/(?P<answer>[0-9]+)$',
        views.characterboon_validation, name='characterboon_validation'),

    # Create / Create one charactersheet
    #  ex: /domainmanager/character_create
    url(r'^character_create/', views.character_create, name='character_create'),
    # Create / Edit one charactersheet

    #  ex: /domainmanager/characterinformation/1/edit
    url(r'^characterinformation/(?P<character_id>[0-9]+)/edit/', views.characterinformation_edit, name='characterinformation_edit'),

    # Create / Edit one character's properties
    #  ex: /domainmanager/characterproperties/1/edit
    url(r'^characterproperties/(?P<character_id>[0-9]+)/edit/', views.characterproperties_edit, name='characterproperties_edit'),

    # Buy new character stuff e.g. disciplines, rituals, etc...
    #  ex: /domainmanager/charactershopping/1
    url(r'^charactershopping/(?P<character_id>[0-9]+)/buy', views.charactershopping, name='charactershopping'),

    # View character stuff in your basket e.g. disciplines, rituals, etc...
    #  ex: /domainmanager/characterbasket/1
    url(r'characterbasket/(?P<character_id>[0-9]+)', views.characterbasket, name='characterbasket'),

    # List of all players
    #  ex: /domainmanager/players
    url(r'^players$', views.players, name='players'),

    # List all the characters
    # ex: /domainmanager/playersummary/1
    url(r'^playersummary/(?P<player_id>[0-9]+)$', views.playersummary, name='playersummary'),

    # View of the genealogy
    #  ex: /domainmanager/genealogy
    url(r'^genealogy$', views.genealogy, name='genealogy'),

    #############################################################ADMINAREA#############################################################

    # Admin view for all boons
    #  ex: /domainmanager/adminboons
    url(r'^adminboons$', views.adminboons, name='adminboons'),

    # Admin view for all baskets (stuff players want to buy)
    #  ex: /domainmanager/adminbasket
    url(r'^adminbasket', views.adminbasket, name='adminbasket'),

    # Admin edit form for all baskets (stuff players want to buy)
    #  ex: /domainmanager/adminshopping_validation
    url(r'^adminshopping_validation/(?P<property_id>[0-9]+)/(?P<hash>[A-Za-z0-9]+)/(?P<answer>[0-9]+)$',
        views.adminshopping_validation, name='adminshopping_validation'),

    # Validate boons as a GM
    #  ex: /domainmanager/adminboon_validation/1/1bfkdjbf/2
    url(r'^adminboon_validation/(?P<boon_id>[0-9]+)/(?P<hash>[A-Za-z0-9]+)/(?P<answer>[0-9]+)$',
        views.adminboon_validation, name='adminboon_validation'),

    #############################################################SYSTEM#############################################################


    # Logout
    #  ex: /domainmanager/logout
    url(r'^logout', views.logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
