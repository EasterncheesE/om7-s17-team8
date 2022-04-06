from django.views import generic
from author.forms import *
from author.models import Author
from django.shortcuts import render, redirect


class AuthorListView(generic.ListView):

    model = Author
    context_object_name = "authors"
    template_name = 'author/list.html'


class AuthorDetailView(generic.DetailView):

    model = Author
    context_object_name = "author"
    template_name = 'author/detail.html'


def author_form(request, id=None):
    if request.method == "GET":
        if id:
            author = Author.objects.get(pk=id)
            form = AuthorForm(instance=author)
            return render(request, "author/author_form.html", {'form': form})
        else:
            form = AuthorForm()
            return render(request, "author/author_create.html", {'form': form})

    elif request.method == "POST":
        if "delete" in request.POST:
            author = Author.objects.get(pk=id)
            author.delete()
            return redirect(f'/author/all')
        if id:
            author = Author.objects.get(pk=id)
            form = AuthorForm(request.POST, instance=author)
        else:
            form = AuthorForm(request.POST)
        if form.is_valid():
            id = form.save().pk
        if id:
            return redirect(f'/author/{id}')
        else:
            return redirect(f'/author/all')