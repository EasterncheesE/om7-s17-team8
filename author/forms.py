from django import forms
from .models import Author, models


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'surname', 'patronymic')
        labels = {
            'name': 'First Name',
            'surname': 'Last Name',
            'patronymic': 'Patronymic',
        }
