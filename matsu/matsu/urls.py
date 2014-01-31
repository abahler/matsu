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
    url(r'^file-not-found/', 'contactform.views.file_not_found'),
    url(r'^server-error/', 'contactform.views.server_error'),
    url(r'pdf/matsu-workflow-v4.pdf', 'contactform.views.workflow_pdf'),
)
