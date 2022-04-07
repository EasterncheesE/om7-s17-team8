from django.shortcuts import render, redirect
from django.views import generic
from .models import *
from .forms import *


class CustomUserListView(generic.ListView):

    model = CustomUser
    context_object_name = "users"
    template_name = 'customuser/list.html'


class CustomUserDetailView(generic.DetailView):  # Використовуємо DetailView, бо він сам дістає юзера по pk
    model = CustomUser
    context_object_name = 'user'
    template_name = 'customuser/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CustomUserDetailView, self).get_context_data(**kwargs)
        user = self.get_object()
        books = set(map(lambda order: order.book, user.orders.all()))
        context['books'] = books

        return context


def customuser_form(request, id=None):
    if request.method == "GET":
        if id:
            customuser = CustomUser.objects.get(pk=id)
            form = CustomUserForm(instance=customuser)
            return render(request, "customuser/customuser_form.html", {'form': form})
        else:
            form = CustomUserForm()
            return render(request, "customuser/customuser_create.html", {'form': form})

    elif request.method == "POST":
        if "delete" in request.POST:
            customuser = CustomUser.objects.get(pk=id)
            customuser.delete()
            return redirect(f'/user/all')
        if id:
            customuser = CustomUser.objects.get(pk=id)
            form = CustomUserForm(request.POST, instance=customuser)
        else:
            form = CustomUserForm(request.POST)
        if form.is_valid():
            id = form.save().pk
        if id:
            return redirect(f'/user/{id}')
        else:
            return redirect(f'/user/all')