"""template3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from template3.apps.core.views import Dashboard, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard', Dashboard.as_view(), name='dashboard'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    # this should be last
    path('page/', include('django.contrib.flatpages.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve,
                {'document_root': settings.MEDIA_ROOT}),
        path('__debug__/', include(debug_toolbar.urls))
    ]
