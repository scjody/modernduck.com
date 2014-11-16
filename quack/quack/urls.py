from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^tetristats/', include('tetristats.urls', namespace='tetristats')),

    url(r'^admin/', include(admin.site.urls)),
) + staticfiles_urlpatterns()
