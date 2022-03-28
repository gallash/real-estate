import datetime
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from .models import Rented, Place


# class PlaceForm(forms.ModelForm):
#     class Meta:
#         model = Place
#         fields = ['state', 'city', 'street', 'number', 'zip_code', 'garage']

HOUSE_FIELDS = ['state', 'city', 'street', 'number', 'zip_code',
    'living_rooms', 'kitchens', 'bathrooms','bedrooms', 'garage', 
    'description', 'price']

APPARTMENT_FIELDS = ['state', 'city', 'street', 'number', 'zip_code', 
    'living_rooms', 'kitchens', 'bathrooms','bedrooms', 'garage', 
    'building_name', 'floor', 'bloc', 'appartment_number',
    'description', 'price']

KITNET_FIELDS = ['state', 'city', 'street', 'number', 'zip_code', 
    'living_rooms', 'kitchens', 'bathrooms','bedrooms', 'garage', 
    'building_name', 'floor', 'bloc', 'appartment_number',
    'description', 'price']


    


class HousePlaceForm(forms.ModelForm): # Expressamente assinalar tipo como Casa
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['price'].required = True
        # self.fields['type_of_place']

    class Meta:
        model = Place
        # Posso assinalar valores assim? 
        # model.pk = 
        # model.type_of_place = 

        fields = HOUSE_FIELDS

class AppartmentPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = APPARTMENT_FIELDS

class KitnetPlaceForm(forms.ModelForm): # Studio Appartment
    class Meta:
        model = Place
        fields = KITNET_FIELDS


class RentedForm(forms.ModelForm):
    user = User
    place = Place
    class Meta:
        model = Rented
        fields = ['start_date', 'end_date', 'user_comment']


class UserRegistrationForm(UserCreationForm):
    # phone = forms.IntegerField() # max_length=13
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,13}$', message="O número de telefone deve estar no formato '+999999999999'")
    phone = forms.CharField(validators=[phone_regex], max_length=17)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'password1', 'password2']


# class ExpressionInterestForm(forms.Form):
