from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'contactform.views.home'),
    url(r'^about/$', 'contactform.views.home'),
    url(r'^web-applications/', 'contactform.views.webapps'),
    url(r'^contact/', 'contactform.views.contact'),
    url(r'^matsu-demos/', 'contactform.views.matsu_demos')
    # Deliberately omitted redirect for "thank you" page since we don't want users visiting directly
)
