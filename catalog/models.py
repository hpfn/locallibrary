from django.db import models
from django.urls import reverse  # used to generate URLs by reversing


# Create your models here.
class Language(models.Model):
    """ language (python, C, ShellScript) """
    language = models.CharField(max_length=30, help_text="programming language")

    def __str__(self):
        """ String for representing the Model object """
        return self.language


class Topic(models.Model):
    """ topic (OOP, Forensis, ALgorithms, etc """
    topic = models.CharField(max_length=50, help_text="book is about?")

    def __str__(self):
        return self.topic


class Book(models.Model):
    """ Representing a book """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can
    # Author as a string rather than object because it hasn't been declared ye
    # on_delete=models.SET_NULL, which will set the value of the author to 
    # Null if the associated author record is deleted.
    summary = models.TextField(max_length=1000,
                               help_text="Enter a brief description")
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character')
    language = models.ManyToManyField(Language,
                                      help_text="Select a programming language for this book")
    topic = models.ManyToManyField(Topic,
                                   help_text="Select a topic for this book")
    # ManyToManyField used because genre can contain many books.
    # Genre class has already been defined so we can specify the object above.
    # The genre is a ManyToManyField, so that a book can have multiple genres
    # and a genre can have many books. The author is declared as ForeignKey, 
    # so each book will only have only one author, but an author may have many
    # books (in practice a book might have multiple authors, but not in this 
    # implementation!)
    ebook = models.FileField(upload_to='documents/', default='ebook_XXX.pdf')
    image = models.FileField(upload_to='img/', default='ebook_img.jpeg')

    class Meta:
        ordering = ('title',)

    def __str__(self):
        """ Representing the Model object """
        return self.title

    def get_absolute_url(self):
        """ returns the url to access a particular book instance """
        return reverse('book-detail', args=[str(self.id)])

    # The model also defines __str__() , using the book's title field to 
    # represent a Book record. The final method, get_absolute_url() returns 
    # an URL that can be used to access a detail record for this model (for 
    # this to work we will have to define a URL mapping that has the name 
    # book-detail, and define an associated view and template).

    def display_language(self):
        """
        Creates a string for the Language. This is required to display 
        language in Admin
        """
        return ', '.join([language.language
                          for language in self.language.all()[:5]])

    display_language.short_description = 'Language'

    def display_topic(self):
        """
        Creates a string for the Topic. This is required to display 
        topic in Admin
        """
        return ', '.join([topic.topic
                          for topic in self.topic.all()[:15]])

    display_topic.short_description = 'Topic'


# import uuid # Required for unique book instances
# class BookInstance(models.Model):
#    """
#    Model representing a specific copy of a book (i.e. that can be borrowed fr
#    """
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4, 
#    help_text="Unique")
#    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
#    imprint = models.CharField(max_length=200)
#    due_back = models.DateField(null=True, blank=True)
#
#    LOAN_STATUS = (
#            ('d', 'Maintenance'),
#            ('o', 'On loan'),
#            ('a', 'Available'),
#            ('r', 'Reserved'),
#    )
#    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, 
#            default="a")
#
#    class Meta:
#        ordering = ["due_back"]
#
#    def __str__(self):
#        """
#        String for representing the Model object
#        """
#        return '%s (%s)' % (self.id,self.book.title)

class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ('last_name',)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)
