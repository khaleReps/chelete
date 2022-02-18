
from django.contrib import admin
from django.urls import path
from website import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('balance', views.balance, name='balance'),

    path('bill', views.bill, name='bill'),
    path('create_invoice', views.create_invoice, name='create_invoice'),
    path('index', views.index, name='index'),
    path('invoice', views.invoice, name='invoice'),

    path('lock', views.lock, name='lock'),
    path('notification', views.notification, name='notification'),
    path('ott', views.otp, name='otp'),
    path('profile', views.profile, name='profile'),
    path('reset', views.reset, name='reset'),

    path('settings_activity', views.settings_activity, name='settings_activity'),
    path('settings_api', views.settings_api, name='settings_api'),
    path('settings_application', views.settings_application, name='settings_application'),
    path('settings_payment_method', views.settings_payment_method, name='settings_payment_method'),
    path('settings_profile', views.settings_profile, name='settings_profile'),
    path('settings_security', views.settings_security, name='settings_security'),


    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),

    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),

]+  static(
    settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT)


