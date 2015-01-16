from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HSAServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^main/', include('main.urls', namespace='main')),
    url(r'^admin/', include(admin.site.urls)),
)
