from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'contactform.views.home'),
    url(r'^about/$', 'contactform.views.home'),
    url(r'^web-applications/', 'contactform.views.webapps'),
    url(r'^contact/$', 'contactform.views.contact'),
    url(r'^contact/thankyou/', 'contactform.views.thankyou'),
    url(r'^matsu-demos/', 'contactform.views.matsu_demos'),
)
