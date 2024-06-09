from django.shortcuts import render,redirect,get_object_or_404
from .forms import room_form
from base.models import hotel
from  django.contrib import messages
from .models import Room,Booking
import re
def home_room(request):
      {% if room in booked_rooms %}
            <h2>booked</h2>
        {% endif %}
    return render(request, 'room/room_home.html',content)

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
        room=form.save(commit=False)
        room.user=request.user
        room.save()
        return redirect("home-room")
    return redirect("create-room")
def delete_room(request,pk):
    room=get_object_or_404(Room,pk=pk)
    if request.method == "POST":
        room.delete()
    # room.delete()
    return render(request,"room/delete.html")
def booking_room(request,pk):
    room=Room.objects.get(id=pk)
    startdate=request.POST.get("startdate")
    enddate=request.POST.get("enddate")
    if request.method == "POST":
        gst=((room.price)*18)/100
        book=room.booking_set.create(
            user=request.user ,
            room=room,
            start_date=startdate,
            end_date=enddate,
            total_price =room.price + gst
        )
        return redirect("home-room")
  
    return render(request,"room/booking_form.html")
    # return render(re)
    