from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import UserProfile
from django.contrib.auth.models import User
from.models import UserProfile
def profile(request,pk):
    user=User.objects.get(id=pk)
    restaurant=user.restaurants_set.all()
    profile=user.userprofile
    content={"user":user,"profile":profile,"restaurant":restaurant}
    return render(request,"accounts/userProfile.html",content)

def update_profile(request,pk):
    profile=UserProfile
    if request.method == "POST":
        username=request.POST.get("username")
        city=request.POST.get("city")
        ProfilePicture=request.FILES.get("image")
        dob=request.POST.get("dob")
        if ProfilePicture:
            user
            profilePicture
            dateOfBirth
            city
                    
    
    
    return render(request,"update_profile.html")
