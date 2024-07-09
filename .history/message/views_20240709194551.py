from django.shortcuts import render,redirect
from base.models import restaurants,dish 
from django.contrib.auth.models import User
from .models import message 
from django.contrib.auth.decorators import login_required
from django.db.models import Q 
from django.contrib import messages  
from django import template
from django.utils import timezone
from django.template.defaulttags import register

def make_dictonery_fun(list_objs):
    return {obj.id : time_since(obj.added) for obj in list_objs}
@login_required(login_url="login-page") 
def message_home(request,rest_id):
    restaurant=restaurants.objects.get(id=rest_id)
    receiver=User.objects.get(id=restaurant.user.id)  
    sender_user=request.user.id
    sender=User.objects.get(id=sender_user)
    message_obj=message.objects.filter(
                                       Q(Q(sender=sender) &Q(receiver=receiver)) |
                                       Q( Q(sender=receiver) & Q(receiver=sender))
                                       )

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
    message_time=make_dictonery_fun(message_obj)
    context={"message_obj":message_obj,"sender":sender,"receiver":receiver,
             "message_time"}
    return render(request,"message/message_home.html",context)

def receiver_list(request,rest_id):
    restaurant=restaurants.objects.get(id=rest_id)
    receivers=message.objects.filter(Q(restaurant=restaurant) & Q(receiver=restaurant.user))
    content={"receivers":receivers,"restaurant":restaurant} 
    return render(request,"message/reciever_list.html",content)
def restaurant_owner_reply(request,receiver_id , sender_id,rest_id):
    sender=User.objects.get(id=sender_id) 
    receiver=User.objects.get(id=receiver_id) 
    restaurant=restaurants.objects.get(id=rest_id) 
    message_obj=message.objects.filter(
                                       Q(Q(sender=sender) &Q(receiver=receiver)) |
                                       Q( Q(sender=receiver) & Q(receiver=sender))
                                       )
    if request.method == "POST":
        message_text=request.POST.get("message")
        message_obj=message.objects.create(
            receiver=receiver,
            sender=sender,
            text=message_text,
            restaurant=restaurant
        )
        message_obj.save()
        return redirect("message-owner",receiver_id=receiver.id ,sender_id=sender.id,rest_id=restaurant.id)
    context={"message_obj":message_obj,"sender":sender,"receiver":receiver}
    return render(request,"message/message_home_owner.html",context)


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
@register.filter
def time_since(value):
    now=timezone.now()
    diff=now-value
    if diff.days == 0:
        if diff.seconds >= 0 and diff.seconds < 60:
            return 'just now'
        if diff.seconds >= 60 and diff.seconds < 3600:
            minutes = diff.seconds // 60
            return f'{minutes} minutes ago'
        if diff.seconds >= 3600 and diff.seconds < 86400:
            hours = diff.seconds // 3600
            return f'{hours} hours ago'
    if diff.days == 1:
        return 'yesterday'
    if diff.days < 7:
        return f'{diff.days} days ago'
    if diff.days < 30:
        weeks = diff.days // 7
        return f'{weeks} weeks ago'
    if diff.days < 365:
        months = diff.days // 30
        return f'{months} months ago'
    years = diff.days // 365
    return f'{years} years ago'