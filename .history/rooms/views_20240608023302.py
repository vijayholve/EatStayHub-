from django.shortcuts import render,redirect
from .forms import room_form
def room(request):
    return render(request, 'room/room_home.html')

def create_room(request):
    
    form=room_form()
    if request.method == "POST":
        form=room_form(request.POST,request.FILES)
        form.save()
        return redirect("room-create")
    return render(request, 'room/create_room.html')