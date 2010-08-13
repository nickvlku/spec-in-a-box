from django.conf.urls.defaults import patterns, include

import spec_in_a_box


urlpatterns = patterns('',
    (r'^spec/', include(spec_in_a_box.urls)),
)
