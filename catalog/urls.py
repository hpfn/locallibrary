from .views import index
from .views import BookListView, BookDetailView
from django.conf.urls import url


urlpatterns = [
        url(r'^$', index, name='index'),
        url(r'^books/$', BookListView.as_view(), name='books'),
        url(r'^books/(?P<pk>\d+)$', BookDetailView.as_view(), name='book-detail'),
]
