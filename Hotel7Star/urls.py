"""Hotel7Star URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from decouple import config
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static


# naming the system
admin.site.site_header = config('ADMIN_APP_SITE_HEADER')
admin.site.index_title = config('APP_NAME')
admin.site.site_title = config('ADMIN_APP_SITE_TITLE')

urlpatterns = [
    path('admin/', admin.site.urls),

    # frontedn routes
    path('', include('apps.frontend.hotel.urls')),

    # backend routes
    path('system/', login_required(TemplateView.as_view(template_name='backend/home/index.html')), name='system'),

    path('system/', include('apps.backend.users.urls')),
    

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


