from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('spec_in_a_box.sample_service',
                       url(r'^login$', 'login_landing_page', name='login_page'),
                       url(r'^logout$', 'logout_landing_page', name='logout_page'),
                       url(r'^sample_service/login$', 'sample_service_login', name='service_login'),      # this is the page defers to the service for login
                       url(r'^sample_service/done$', 'sample_service_done', name='service_done'),         # this is the bounceback url for an OAuth auth (if needed)
                       url(r'^stuff$', 'stuff_view', name='stuff_view')

)
