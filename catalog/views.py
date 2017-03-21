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
    num_authors = Author.objects.count() # The 'all()' is implied by default. ?
    num_languages = Language.objects.count()
    num_topics = Topic.objects.count()

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

class BookDetailView(generic.DetailView):
    model = Book

