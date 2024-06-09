from django.shortcuts import render,redirect,get_object_or_404
from .forms import room_form
from base.models import hotel
from  django.contrib import messages
from .models import Room
import re
def home_room():
    rooms=Room.objects.all()
    for room in rooms:
        print(room.roomNo)
    content={"rooms":rooms}
    # return render(request, 'room/room_home.html',content)

def create_room(request):
    form=room_form()
    if request.method == "POST":
        return _extracted_from_create_room_4(request)
    content={"form":form}
    return render(request, 'room/create_room.html',content)


# TODO Rename this here and in `create_room`
def _extracted_from_create_room_4(request):
    form=room_form(request.POST,request.FILES)
    form.user=request.user

    if form.is_valid():
        form.save() 
        return redirect("home-room")
    return redirect("create-room")
def delete_room(request,pk):
    room=get_object_or_404(Room,pk=pk)
    room.delete()
    return redirect("home-room")
    