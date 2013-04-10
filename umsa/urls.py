from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()
dajaxice_autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'voto.views.index', name='home'),
    url(r'^resultado/$', 'voto.views.result', name='result'),
    # url(r'^umsa/', include('umsa.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)
urlpatterns += staticfiles_urlpatterns()