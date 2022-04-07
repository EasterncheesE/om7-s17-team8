from django import forms
from .models import CustomUser, models


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'middle_name', 'email', 'password', 'role', 'is_active')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'middle_name': 'Middle Name',
            'email': 'Email',
            'password': 'Password',
            'role': 'Role',
            'is_active': "Is active"
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].empty_label = "User first name"
        self.fields['last_name'].empty_label = "User last name"
        self.fields['email'].empty_label = 'User email'
