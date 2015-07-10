from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    #url(r'^$', 'tetristats.views.home', name='home'),
    url(r'^$',
        RedirectView.as_view(url='http://firetetris.com', permanent=False),
        name='home'),
    url(r'^collector$', 'tetristats.views.collector', name='collector'),
    url(r'^stats$', 'tetristats.views.stats', name='stats'),
    url(r'^faq$', 'tetristats.views.faq', name='faq'),
)
