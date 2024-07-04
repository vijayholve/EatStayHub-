from django.shortcuts import render,redirect
from base.models import restaurants,dish 
from django.contrib.auth.models import User
from .models import message 
from django.contrib.auth.decorators import login_required
from django.db.models import Q
@login_required(login_url="login-page")
def message_home(request,pk):
    restaurant=restaurants.objects.get(id=pk)
    receiver=restaurant.user
    sender=request.user
    sender_obj=User.objects.filter(sender=sender)
    receiver_obj=User.objects.filter(receiver=receiver)
    if request.method == "POST":
        message_text=request.POST.get("message")
        message_obj=message.objects.create(
            receiver=receiver,
            sender=sender,
            text=message_text,
            restaurant=restaurant
        )
        message_obj.save()
        return redirect("restaurant-data",pk=restaurant.id)
    context={"receiver":receiver_obj,"sender":sender_obj}
    return render(request,"message/message_home.html",context)