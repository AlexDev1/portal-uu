from django.conf import settings
from django.conf.urls import include, url  # noqa
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

import django_js_reverse.views
from filebrowser.sites import site

from app.core.views import IndexView, SearchGoogle


urlpatterns = [
    path('admin/filebrowser/', site.urls),
    url(r'^admin/', admin.site.urls),
    path('api/autocomplete/', include('uuportal.urls_autocomplete')),
    url(r'^jsreverse/$', django_js_reverse.views.urls_js, name='js_reverse'),
    path('search/', SearchGoogle.as_view(), name='search_google'),
    url(r'^$', IndexView.as_view(), name='home'),
    path('about/', TemplateView.as_view(template_name = 'polo/landing/about.html'), name='about'),
    path('', include(('app.news.urls', 'news'), namespace='news')),
    # path('', include('app.testing.urls', namespace='edu')),
    # path('', include('app.univer.urls')),
    # path('', include('app.college.urls')),
    # path('', include('app.tribune.urls', namespace='blog')),
    # path('', include('app.library.urls', namespace='library')),
    # path('', include('app.competitions.urls', namespace='contest')),
    # path('', include('app.materials.urls')),
    # path('', include('app.schoolsite.urls'),),
    # path('', include('app.users.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
