from msilib.schema import Property

from django.contrib import admin
from django.template.defaultfilters import title


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'address', 'price_per_night', 'created_at')


class Booking:
    pass


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'start_date', 'end_date', 'created_at')
    

