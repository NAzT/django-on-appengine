from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^appproject/', include('appproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^$', 'myapp.views.main'),
    (r'^temp/', 'myapp.views.index'),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
