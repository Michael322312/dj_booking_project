from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Hotel(models.Model):
    name = models.CharField(max_length=63)
    country = models.CharField(max_length=63)
    city = models.CharField(max_length=63)


class Room(models.Model):
    number = models.CharField(max_length=63)
    description = models.TextField()
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits = 1000, decimal_places=1)
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE, related_name="rooms")
    
    def __str__(self):
        return self.number
    
    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ["number"]


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete = models.CASCADE, related_name="booked")
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "booked")

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateField(auto_now = True)


    def __str__(self):
        return self.room.number
    
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["-end_time", "room"]



