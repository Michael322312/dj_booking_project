from django.shortcuts import render
from hotels.models import *
# Create your views here.

def get_rooms_list(request):
    hotels = Hotel.objects.all()

    context = {
        "hotels": hotels,
    }

    return render(
        request,
        "hotel/room_list.html",
        context
    )

def get_users_list(request):
    users = User.objects.all()

    context = {
        "users": users,
    }

    return render(
        request,
        "hotel/users_list.html",
        context
    )