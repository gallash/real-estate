import datetime
from this import d

from django import forms
from django.db import models
from django.contrib.auth.models import User
from .models import Rented, Place


class RentedForm(forms.ModelForm):
    user = User
    place = Place
    class Meta:
        model = Rented
        fields = ['start_date', 'end_date']