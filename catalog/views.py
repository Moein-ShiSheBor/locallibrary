from django.shortcuts import render
from django.views import generic
from .models import *


# def index(request):
#     num_books = Book.objects.all().count()
#     num_instances = BookInstance.objects.all().count()
#     num_instances_available = BookInstance.objects.filter(status__exact='a').count()
#     num_authors = Author.objects.count()
#
#     context = {'num_books': num_books, 'num_instances': num_instances,
#                'num_instances_available': num_instances_available, 'num_authors': num_authors}
#
#     return render(request, 'catalog/index.html', context=context)

class Index(generic.TemplateView):
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_books'] = Book.objects.all().count()
        context['num_instances'] = BookInstance.objects.all().count()
        context['num_instances_available'] = BookInstance.objects.filter(status__exact='a').count()
        context['num_authors'] = Author.objects.count()

        return context


class BookListView(generic.ListView):
    model = Book
    template_name = 'catalog/book_list.html'
    context_object_name = 'book_list'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'
    context_object_name = 'book'


class AuthorListView(generic.ListView):
    model = Author
    template_name = 'catalog/author_list.html'
    context_object_name = 'author_list'
