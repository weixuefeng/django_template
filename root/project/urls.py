"""dapp_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.views.static import serve as serve_static
from django.views.decorators.cache import never_cache


urlpatterns = [
    url('^', include('web.urls')),
    url('^admin/', admin.site.urls),
    url(r'^static/(?P<path>.*)$', never_cache(serve_static), {'document_root': '%s/static' % settings.PROJECT_ROOT, 'show_indexes': True}),
    url(r'^filestorage/(?P<path>.*)$', never_cache(serve_static), {'document_root': '%s' % settings.PROJECT_ROOT, 'show_indexes': True})
]
