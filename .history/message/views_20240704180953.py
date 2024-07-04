from django.shortcuts import render,redirect
from base.models import restaurants,dish 
from django.contrib.auth.models import User
from .models import message 
from django.contrib.auth.decorators import login_required
from django.db.models import Q
@login_required(login_url="login-page")
def message_home(request,rest_id,user_id):
    receiver=User.objects.get(id=user_id)
    restaurant=restaurants.objects.get(id=rest_id) 
    sender=request.user 
    message_obj=message.objects.filter(Q(sender=sender) & Q(restaurant=)
    # user_objs = User.objects.filter(Q(sender_message__receiver=receiver) | Q(receiver_message__sender=sender)).distinct() 
    
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
    context={"message_obj":message_obj,"sender":sender,"receiver":receiver}
    return render(request,"message/message_home.html",context)