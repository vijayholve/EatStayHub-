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
    message_obj=message.objects.filter(Q(sender=sender) & Q(receiver=receiver))[:1]
    user_obj=User.objects.get(Q(message__sender__=sender) & Q(message__receiver))
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
    context={"message_obj":message_obj}
    return render(request,"message/message_home.html",context)