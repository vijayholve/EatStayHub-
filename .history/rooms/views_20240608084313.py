from django.shortcuts import render,redirect
from .forms import room_form
from base.models import hotel
from  django.contrib import messages

def room(request):
    return render(request, 'room/room_home.html')

def create_room(request):
    form=room_form()
    if request.method == "POST":
        return _extracted_from_create_room_4(request)
    content={"form":form}
    return render(request, 'room/create_room.html',content)


# TODO Rename this here and in `create_room`
def _extracted_from_create_room_4(request):
    form=room_form(request.POST)
    if form.is_valid():
        room=form.save(commit=False)
        room.user=request.user
        room.hotels=hotel.objects.get(id=2)
        room.save() 
        return redirect("create-room")
    else:
        messages.error()