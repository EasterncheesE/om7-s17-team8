from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'authors')
        labels = {
            'name': 'Book Name',
            'description': 'Description',
            'count': 'Count',
            'authors': "Author IDs"
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['name'].empty_label = "Book name"
        self.fields['description'].empty_label = "Book description"
        self.fields['count'].empty_label = 1
        self.fields['count'].empty_label = 'Book author IDs'
