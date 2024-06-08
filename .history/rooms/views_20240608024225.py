from django.shortcuts import render,redirect
from .forms import room_form
from base.models import hotel
def room(request):
    return render(request, 'room/room_home.html')

def create_room(request):
    form=room_form()
    if request.method == "POST":
        form=room_form(request.POST)
        forms=form.save(commit=False)
        forms.user=request.user
        forms.hotels=hotel.objects.get(id=2)
        forms.savee()
        return redirect("home-room")
    content={"form":form}
    return render(request, 'room/create_room.html',content)