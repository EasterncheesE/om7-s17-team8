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

    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        self.fields['name'].empty_label = "Author first name"
        self.fields['surname'].empty_label = "Author last name"
        self.fields['patronymic'].empty_label = 'Author patronymic'
