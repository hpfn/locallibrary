from django.shortcuts import render
from django.http import HttpResponse


# request is not used, but is necessary
# 'got multiple values for argument' error
def show_pdf(request, pdf_file):
    from catalog.models import Book
    # file = Book.objects.get(title='TITLE HERE')
    file = Book.objects.get(title=pdf_file)
    #print(file.ebook.path)
    path_to_pdf = file.ebook.path
    #from django.conf import settings
    #path_to_pdf = settings.MEDIA_ROOT + '/documents/' + pdf_file
    with open(path_to_pdf, 'rb') as ebook:
        response = HttpResponse(ebook.read(), content_type='application/pdf')
        response['Content-Disposition'] = "inline; filename=" + pdf_file
        return response
