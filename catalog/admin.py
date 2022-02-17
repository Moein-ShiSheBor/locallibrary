from django.contrib import admin
from .models import *


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        ("Information", {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        })
    )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('first_name', 'last_name')
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # list_filter = ()
    list_display = ('title', 'author', 'display_genre')
    # fields = ['title', 'author', 'summary', 'genre', 'isbn']
    # --> if we don't write this it will make it itself by the order that we write in models
    inlines = [BookInstanceInline]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
