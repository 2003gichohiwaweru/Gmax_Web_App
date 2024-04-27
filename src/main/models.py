import uuid
from django.db import models

from users.models import Profile, Location
from .consts import CAR_BRANDS, TRANSMISSION_OPTIONS
from .utils import user_listing_path
# Create your models here.
class Listing(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    brands = models.CharField(default=None, max_length=24, choices=CAR_BRANDS)
    model = models.CharField(max_length=64,)
    vin = models.CharField(max_length=16,)
    mileage = models.IntegerField(default=0)
    color = models.CharField(max_length=24)
    description = models.TextField()
    engine = models.CharField(max_length=24)
    transmission = models.CharField(max_length=24, choices=TRANSMISSION_OPTIONS, default=None)

    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=user_listing_path)



    def __str__(self):
        return f'{self.seller.user.username} Listing\'s - {self.model}'