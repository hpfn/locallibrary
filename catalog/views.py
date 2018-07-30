from django.shortcuts import render
from django.views import generic

from .models import Book, Author, Language, Topic


# Create your views here.
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default. ?
    prog_lang = Language.objects.values_list('language')  # count()
    topics = Topic.objects.values_list('topic')

    num_languages = [pl[0] for pl in prog_lang]
    num_topics = [t[0] for t in topics]

    template_name = 'index.html'
    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_languages': num_languages,
        'num_topics': num_topics,
    }

    # Render the HTML template index.html with the data in the context variabl
    return render(request, template_name, context)


# class-based view: tutorial 6
# Django best-practice
class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

    # queryset = Book.objects.filter(title__icontains= formulario aqui)


class BookDetailView(generic.DetailView):
    model = Book


class AuthorsListView(generic.ListView):
    model = Author
    paginate_by = 10


class SelectBooksListView(generic.ListView):
    model = Book

    def get_queryset(self):
        return Book.objects.filter(title__icontains=self.request.GET['language'])
