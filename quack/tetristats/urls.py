from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'tetristats.views.home', name='home'),
)
