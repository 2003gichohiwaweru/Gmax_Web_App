from django import forms
from django.db import models
from localflavor.us.models import USStateField, USZipCodeField

from .models import Location


class LocationForm(forms.ModelForm):
    address_1 = forms.CharField(required =True)
    



    class Meta:
        model = Location
        fields = {'address_1', 'address_2', 'city','state', 'zip_code'}