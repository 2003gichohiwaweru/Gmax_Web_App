from django.db import models
from django.contrib.auth.models import User 
from localflavor.us.models import USStateField, USZipCodeField
from .utils import user_directory_path


class Location(models.Model):
    address_1 = models.CharField(max_length=128, blank=True)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64)
    state = USStateField(default="NY")
    zip_code = USZipCodeField(blank=True)

    def __str__(self):
        return f'Location {self.id}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(null=True, upload_to=user_directory_path, height_field=None, width_field=None, max_length=None)
    bio = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True, related_name='profile')

    def __str__(self):
        return f'Profile for {self.user.username}'
