from .views import index
from .views import BookListView, BookDetailView
from .views import AuthorsListView
from .views import SelectBooksListView
from django.urls import path, re_path


urlpatterns = [
        path('', index, name='index'),
        path('books/', BookListView.as_view(), name='books'),
        re_path(r'^books/(?P<pk>\d+)$', BookDetailView.as_view(), name='book-detail'),
        re_path(r'^authors/$', AuthorsListView.as_view(), name='authors'),
        re_path(r'^select_books/$', SelectBooksListView.as_view(), name='select_books'),
]
