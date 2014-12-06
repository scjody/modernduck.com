from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'tetristats.views.home', name='home'),
    url(r'^collector$', 'tetristats.views.collector', name='collector'),
    url(r'^show$', 'tetristats.views.show', name='show'),
)
