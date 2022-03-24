from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm # Premade template


# Use django-phonenumber-field? OR django-phone-field?


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def validate_phone_number(self):
        pass