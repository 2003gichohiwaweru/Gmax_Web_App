from .models import Listing
import django_filters

class ListingFilter(django_filters.FilterSet):

    class Meta:
        model = Listing
        fields = {'brands': {'exact'}, }