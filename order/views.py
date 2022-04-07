from django.views import generic
from django.db.models import F
from order.models import Order
from authentication.models import CustomUser
from book.models import Book
from datetime import datetime
from django.shortcuts import render, redirect
import pytz
from .forms import *


class OrderListView(generic.ListView):

    model = Order
    context_object_name = "orders"
    template_name = 'order/list.html'


class SortedOrderView(generic.ListView):
    template_name = 'order/sorted.html'
    context_object_name = 'orders'

    def get_queryset(self):
        param = self.request.GET.get('param', '?')
        sorting = self.request.GET.get('sorting')
        queryset = Order.objects.order_by(param)

        if sorting == 'asc':
            return queryset

        return queryset.reverse()


class OrderDebtorsView(generic.ListView):
    context_object_name = 'users'
    template_name = 'order/debtors.html'

    def get_queryset(self):
        late_returners = Order.objects.filter(end_at__gte=F('plated_end_at')).values_list("user_id", flat=True)
        debtors = Order.objects.filter(end_at=None).values_list("user_id", flat=True).filter(plated_end_at__gte=datetime.now(tz=pytz.UTC))

        return CustomUser.objects.all().filter(pk__in=late_returners|debtors).order_by("pk")


def order_form(request, id=None):
    if request.method == "GET":
        if id:
            order = Order.objects.get(pk=id)
            form = OrderForm(instance=order)
            return render(request, "order/order_form.html", {'form': form})
        else:
            form = OrderForm()
            return render(request, "order/order_create.html", {'form': form})

    elif request.method == "POST":
        if "delete" in request.POST:
            order = Order.objects.get(pk=id)
            order.delete()
            return redirect(f'/order/all')
        if id:
            order = Order.objects.get(pk=id)
            form = OrderForm(request.POST, instance=order)
        else:
            form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            id = order.id
        return redirect(f'/order/all')