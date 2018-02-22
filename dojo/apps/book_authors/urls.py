from django.conf.urls import url
import views

urlpatterns = [
    url(r'book_authors', views.books),
]