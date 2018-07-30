"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from locallibrary.views import show_pdf

#my_app = 'locallibrary'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='/catalog', permanent=True)),
    # url(r'^media/documents/(?P<pdf_file>[-\w]+\.pdf)$', show_pdf, name='show_pdf'),
    #url(r'^media/documents/(?P<pdf_file>.*)$', show_pdf, name='show_pdf'),
    re_path('locallibrary/(?P<book_title>.*)$', show_pdf, name='show_pdf'),
    re_path(r'^media/(?P<path>.*\.jpeg)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
