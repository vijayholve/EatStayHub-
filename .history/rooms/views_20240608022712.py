from django.shortcuts import render

def room(request):
    return render(request, 'room/room_home.html')

def create_room(request):
    
    return render(request, 'room/create_room.html')