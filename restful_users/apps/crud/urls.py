from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'users$', views.index, name="crud_index"),
    url(r'users/new$', views.new, name="crud_new"),
    url(r'users/(?P<id>\d+)/edit$', views.edit, name="crud_edit"),
    url(r'users/(?P<id>\d+)$', views.show, name="crud_show"),
    url(r'^users/create$', views.create),
    url(r'users/(?P<id>\d+)/destroy$', views.destroy, name="crud_destroy"),
    url(r'users/update$', views.update, name="crud_update"),
]