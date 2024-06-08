from django.shortcuts import render
from .forms import room_form
def room(request):
    return render(request, 'room/room_home.html')

def create_room(request):
    form=room_form
    return render(request, 'room/create_room.html')