from django.conf.urls import url

from . import views

app_name = 'domainmanager'

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),

]
