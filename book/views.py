from django.views import generic
from book.filters import BookFilter
from author.models import Author
from django.shortcuts import render, redirect
from book.forms import *


class BookListView(generic.ListView):

    model = Book
    context_object_name = "books"
    template_name = 'book/list.html'


class BookDetailView(generic.DetailView):

    model = Book
    context_object_name = "book"
    template_name = 'book/detail.html'


class UnorderedBookView(generic.ListView):

    context_object_name = 'books'
    template_name = 'book/list.html'
    extra_context = {"show_count": True}

    def get_queryset(self):

        return Book.objects.filter(count__gt=0)


class SortedBookView(generic.ListView):

    template_name = 'book/sorted.html'
    context_object_name = 'books'

    def get_queryset(self):

        param = self.request.GET.get('param', '?')
        sorting = self.request.GET.get('sorting')
        queryset = Book.objects.order_by(param)

        if sorting == 'asc':
            return queryset
        return queryset.reverse()


class FilterBooksView(generic.TemplateView):

    template_name = 'book/filter.html'

    def get_context_data(self, **kwargs):
        context = super(FilterBooksView, self).get_context_data(**kwargs)
        context['filter'] = BookFilter(self.request.GET, queryset=Book.objects.all())
        print(context['filter'].form)
        return context


def book_form(request, id=None):
    if request.method == "GET":
        if id:
            book = Book.objects.get(pk=id)
            form = BookForm(instance=book)
            return render(request, "book/book_form.html", {'form': form})
        else:
            form = BookForm()
            return render(request, "book/book_create.html", {'form': form})

    elif request.method == "POST":
        if "delete" in request.POST:
            book = Book.objects.get(pk=id)
            book.delete()
            return redirect(f'/book/all')
        if id:
            book = Book.objects.get(pk=id)
            form = BookForm(request.POST, instance=book)
        else:
            form = BookForm(request.POST)
        if form.is_valid():
            authors = Author.objects.all().filter(id__in=form.data['authors'])
            book = form.save()
            id = book.id
        if id:
            return redirect(f'/book/{book.id}')
        else:
            return redirect(f'/book/all')