from django.conf import settings
from django.conf.urls import include, url  # noqa
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

import django_js_reverse.views
from filebrowser.sites import site


urlpatterns = [
    path('admin/filebrowser/', site.urls),
    url(r'^admin/', admin.site.urls),
    path('api/autocomplete/', include('uuportal.urls_autocomplete')),
    url(r'^jsreverse/$', django_js_reverse.views.urls_js, name='js_reverse'),

    url(r'^$', TemplateView.as_view(template_name='exampleapp/itworks.html'), name='home'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
