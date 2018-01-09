from django.shortcuts import render
from django.http import HttpResponse


# request is not used, but is necessary
# 'got multiple values for argument' error
def show_pdf(request, book_title):
    from catalog.models import Book
    # file = Book.objects.get(title='TITLE HERE')
    file = Book.objects.get(title=book_title)
    #print(file.ebook.path)
    path_to_pdf = file.ebook.path
    #from django.conf import settings
    #path_to_pdf = settings.MEDIA_ROOT + '/documents/' + pdf_file
    with open(path_to_pdf, 'rb') as ebook:
        read_ebook = ebook.read()

    response = HttpResponse(read_ebook, content_type='application/pdf')
    response['Content-Disposition'] = "inline; filename=" + book_title.replace(' ', '_')
    return response
