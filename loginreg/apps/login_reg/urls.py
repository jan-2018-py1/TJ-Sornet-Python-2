from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'logout$', views.logout),
    url(r'register$', views.register),
    url(r'login$', views.login),
    url(r'success$', views.success),
]