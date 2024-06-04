from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import UserProfile

def profile(request,pk):
    user=User.objects.get(id=pk)
    profile=user.userprofile
    content={"user":user,"profile":profile}
    return render(request,"accounts/userProfile.html",content)