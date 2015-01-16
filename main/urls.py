__author__ = 'Hossein Noroozpour'
from django.conf.urls import patterns, url
from main import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^show/$', views.show, name='show'),
    url(r'^(?P<agent_id>\d+)/detail/$', views.detail, name='detail'),
    )