from django.contrib import admin
from hotels.models import Hotel, Room, Booking
# Register your models here.

admin.site.register(Room)
admin.site.register(Hotel)
admin.site.register(Booking)
