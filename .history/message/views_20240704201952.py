from django.shortcuts import render,redirect
from base.models import restaurants,dish 
from django.contrib.auth.models import User
from .models import message 
from django.contrib.auth.decorators import login_required
from django.db.models import Q
@login_required(login_url="login-page") 
def message_home(request,rest_id):
    restaurant=restaurants.objects.get(id=rest_id)
    sender=request.user 
    receiver=restaurant.user 
    senders_objs=message.objects.filter(Q(restaurant=restaurant) & Q(sender=sender))
    message_obj=message.objects.filter(Q(restaurant=restaurant) & Q(sender=sender) &  Q(receiver=receiver))
    if request.method == "POST":
        message_text=request.POST.get("message")
        message_obj=message.objects.create(
            receiver=receiver,
            sender=sender,
            text=message_text,
            restaurant=restaurant
        )
        message_obj.save()
        return redirect("message-home",rest_id=restaurant.id)
    context={"message_obj":message_obj,"sender":sender,"receiver":receiver}
    return render(request,"message/message_home.html",context)


def all_reciever_message(request,id):
    restaurant=restaurants.objects.get(id=id) 
    sender_list=message.objects.filter(restaurant=restaurant).values('sender__username').distinct()
    sender_list=sender_list["sender_username"]
    context={"sender_list":sender_list}
    return render(request,"message/list_message.html",context)