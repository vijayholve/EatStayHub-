from django.shortcuts import render,redirect,get_object_or_404
from .forms import room_form
from base.models import hotel
from  django.contrib import messages
from .models import Room,Booking
import re
from datetime import datetime
def home_room(request):
    rooms = Room.objects.all()
    booked_rooms = []
    for room in rooms:
        try:
            Booking.objects.get(room=room)
            booked_rooms.append(room)
        except Booking.DoesNotExist:
            pass
    content = {'rooms': rooms, 'booked_rooms': booked_rooms}
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
    startdate=request.GET.get("startdate")
    enddate=request.GET.get("enddate")
    gst=int(((room.price)*18)/100)
    if startdate:
        start_datetime = datetime.strptime(startdate, '%Y-%m-%d')
    if enddate:
        end_datetime = datetime.strptime(enddate, '%Y-%m-%d')
    duration=0
    
    if duration := request.GET.get("{% extends "base/main.html" %}
{% load static  %}
{% block css_content %}
<link rel="stylesheet" href="{% static 'room/booking_room.css' %}?v={{time}}">
{% endblock css_content %}
{% block content %}
<div class="container">
    <div class="main-container">
        <form method="GET" action="">
            {% csrf_token%}
            <div class="data">
                <div class="image">  
                    <img src="/media/{{room.roomImage}}" alt="">
                </div>
                <div class="price">
                    <h2>{{room.roomNAme}}</h2>
                    <h3>Type: {{room.roomType}}</h3>
                    <h3>Location: {{room.location}}</h3>
                    <h4>Price: {{room.price}} and GST of 18% is {{gst}}</h4>
                    <h3>Total Cost: {{total}}</h3>
                </div>
                <div class="sedate">
                    <label for="startdate">Start date:</label>
                    <input type="date" id="startdate" name="startdate" onchange="calculateDuration()"><br>
                    <label for="enddate">End Date:</label>
                    <input type="date" id="enddate" name="enddate" onchange="calculateDuration()"><br>
                    <h3 id="duration"></h3>
                </div>
                <input type="submit" value="Book Room at {{total}}"><br>
            </div>
        </form>
    </div>
</div>

<script>
function calculateDuration() {
    var startdate = document.getElementById("startdate").value;
    var enddate = document.getElementById("enddate").value;

    if (startdate && enddate) {
        var start = new Date(startdate);
        var end = new Date(enddate);
        var duration = (end - start) / (1000 * 3600 * 24);
        document.getElementById("duration").innerHTML = "Duration: " + duration + " days";
    }
}
</script>

{% endblock content %}
"):
        
    if request.method == "GET":
        book=room.booking_set.create(
            user=request.user,
            room=room,
            start_date=startdate,
            end_date=enddate,
            total_price =(room.price + gst)*duration
        )
        return redirect("home-room")
    content={"room":room,"gst":gst,"total":int(room.price+gst),"duration":duration}
    return render(request,"room/booking_form.html",content)
    