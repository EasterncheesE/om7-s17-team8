from django import forms
from .models import Order
from datetime import datetime


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('user', 'book', 'end_at', 'plated_end_at')
        labels = {
            'user': 'User',
            'book': 'Book',
            'end_at': f'Return date, format example: 2021-05-22 11:59:59',
            'plated_end_at': "Planned return date, format example: 2021-05-22 11:59:59"
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['user'].label_from_instance = lambda obj: f'{obj.first_name} {obj.last_name}'
        self.fields['book'].label_from_instance = lambda obj: obj.name
