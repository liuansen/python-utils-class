# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from router import router, router_no_slash


urlpatterns = [
]

urlpatterns += [
    url(r'', include(router.urls)),
    url(r'', include(router_no_slash.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
