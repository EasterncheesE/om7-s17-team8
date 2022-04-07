from django.views import generic
from django.db.models import F
from order.models import Order
from authentication.models import CustomUser
from datetime import datetime
import pytz


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
