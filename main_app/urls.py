__author__ = 'milu'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

)
