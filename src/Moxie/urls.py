from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$','Moxie.views.home', name='home'),
                       url(r'^job$','Moxie.views.job', name='job'),
                       url(r'^load$','Moxie.views.load', name='load'),
                       url(r'^stopped$','Moxie.views.reset', name='stopped'),
                       url(r'^reset$','Moxie.views.reset', name='reset'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
