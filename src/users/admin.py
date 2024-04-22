from django.contrib import admin
from .models import Profile, Location

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'phone_number']
    search_fields = ['user__username', 'bio', 'phone_number']

class LocationAdmin(admin.ModelAdmin):
    list_display = ['address_1', 'city', 'state', 'zip_code']
    search_fields = ['address_1', 'city', 'state', 'zip_code']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Location, LocationAdmin)
