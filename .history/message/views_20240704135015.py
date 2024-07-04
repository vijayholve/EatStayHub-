from django.shortcuts import render,redirect
from base.models import restaurants,dish 
from django.contrib.auth.models import User
from .models import message 
from django.contrib.auth.decorators import login_required

@login_required(login_url="login-page")
def message_home(request,pk):
    restaurant=restaurants.objects.get(id=pk)
    
    if request.method == "POST":
        receiver=restaurant.user
        message_text=request.POST.get("message")
        sender=request.user 
        message_obj=message.objects.create(
            receiver=receiver,
            sender=sender,
            text=message_text,
            restaurant=restaurant
        )
        message_obj.save()
        return redirect("restaurant-data",pk=restaurant.id)
    return render(request,"message/message_home.html")