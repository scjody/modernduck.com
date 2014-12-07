from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'tetristats.views.home', name='home'),
    url(r'^collector$', 'tetristats.views.collector', name='collector'),
    url(r'^stats$', 'tetristats.views.stats', name='stats'),
    url(r'^faq$', 'tetristats.views.faq', name='faq'),
)
