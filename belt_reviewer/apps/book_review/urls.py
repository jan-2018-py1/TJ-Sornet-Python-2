from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'register$', views.register),
    url(r'login$', views.login),
    url(r'books$', views.books),
    url(r'logout$', views.logout),
    url(r'books/add$', views.add),
    url(r'books/create$', views.create),
    url(r'books/(?P<id>\d+)$', views.show_book, name="book_show"),
    # url(r'users/(?P<id>\d+)$', views.show_user, name="user_show"),
    # url(r'books/delete/(?P<id>\d+)$', views.destroy),
]