from django.shortcuts import render
from django.http import HttpResponse

def show_pdf(request, pdf_file):
    print(pdf_file)
    path_to_pdf = 'media/documents/' + pdf_file
    with open(path_to_pdf, 'rb') as ebook:
        response = HttpResponse(ebook.read(), content_type='application/pdf')
        response['Content-Disposition'] = "inline; filename=" + pdf_file
        return response
