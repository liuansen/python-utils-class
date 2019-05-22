# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.conf.urls import include, url

from common.api_docs_utils import get_swagger_view

admin.autodiscover()

urlpatterns = [
    url(r'^api/v1/', include('web.api_urls')),
    url(r'^docs/', get_swagger_view(title='My great API')),
    url(r'^__admin__/', include(admin.site.urls)),
]
