from django.contrib import admin

from .models import Author, Language, Topic, Book  # , BookInstance


# Register your models here.

# admin.site.register(Book)
# for the purpose of this demonstration, we'll
# instead use the @register decorator to register 
# the models (this does exactly the same thing as
# the admin.site.register() syntax):
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_language', 'display_topic')


# display_* are functions. read Mozilla_Django/django_4.pdf.
# check models.py

# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')


admin.site.register(Author, AuthorAdmin)

admin.site.register(Language)
admin.site.register(Topic)
# admin.site.register(BookInstance)
