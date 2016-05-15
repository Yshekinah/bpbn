from django.conf.urls import url

from . import views

app_name = 'domainmanager'

urlpatterns = [
    # ex: /domainmanager/
    url(r'^$', views.index, name='index'),

    # ex: /domainmanager/charactersheet/1
    # View the charactersheet
    url(r'^charactersheet/(?P<character_id>[0-9]+)$', views.charactersheet, name='charactersheet'),

    # ex: /domainmanager/playersummary/1
    # List all the characters
    url(r'^playersummary/(?P<player_id>[0-9]+)$', views.playersummary, name='playersummary')

]
