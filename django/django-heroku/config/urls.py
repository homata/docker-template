"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.urls import include
from django.conf import settings

# from django.utils.translation import ugettext as ugettext_lazy
# from django.views.generic.base import RedirectView
from rest_framework.authtoken import views as auth_views

# Change admin site title
# admin.site.site_title = ugettext_lazy('Login')
# admin.site.site_header = ugettext_lazy('Web App Admin Page')
# admin.site.index_title = ugettext_lazy('Main Menu')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/api-token-auth/', auth_views.obtain_auth_token),

    path('', include('apps.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns