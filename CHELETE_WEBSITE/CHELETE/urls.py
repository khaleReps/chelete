"""CHELETE URL Configuration

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
from django.urls import include, path

from website import urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('balance/', include('website.urls')),
    path('bill/', include('website.urls')),
    path('create_invoice/', include('website.urls')),
    path('index/', include('website.urls')),
    path('invoice/', include('website.urls')),
    path('lock/', include('website.urls')),
    path('notification/', include('website.urls')),

    path('otp/', include('website.urls')),
    path('profile/', include('website.urls')),
    path('reset/', include('website.urls')),

    path('settings_activity/', include('website.urls')),
    path('settings_api/', include('website.urls')),
    path('settings_application/', include('website.urls')),
    path('settings_payment_method/', include('website.urls')),
    path('settings_profile/', include('website.urls')),
    path('settings_security/', include('website.urls')),
    
    path('signin/', include('website.urls')),
    path('signup/', include('website.urls')),


    path('', include('website.urls')),
    path('home/', include('website.urls')),
    path('dasboard/', include('website.urls')),
    



]
