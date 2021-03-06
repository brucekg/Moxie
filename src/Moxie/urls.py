from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^getlogins/oss$','Moxie.views.job', name='job'),
                       url(r'^job$','Moxie.views.job', name='job'),
                       url(r'^set$','Moxie.views.param', name='set'),
                       url(r'^local$','Moxie.views.local', name='local'),
                       url(r'^record$','Moxie.views.record', name='record'),
                       url(r'^load$','Moxie.views.load', name='load'),
                       url(r'^stopped$','Moxie.views.reset', name='stopped'),
                       url(r'^reset$','Moxie.views.reset', name='reset'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
