from .views import index
from .views import BookListView, BookDetailView
from .views import AuthorsListView
from .views import SelectBooksListView
from django.conf.urls import url


urlpatterns = [
        url(r'^$', index, name='index'),
        url(r'^books/$', BookListView.as_view(), name='books'),
        url(r'^books/(?P<pk>\d+)$', BookDetailView.as_view(), name='book-detail'),
        url(r'^authors/$', AuthorsListView.as_view(), name='authors'),
        url(r'^select_books/$', SelectBooksListView.as_view(), name='select_books'),
]
