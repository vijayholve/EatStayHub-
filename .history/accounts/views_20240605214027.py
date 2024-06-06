from django.shortcuts import render,redirect
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
    profile=UserProfile.objects.get(id=pk)
    if request.method == "POST":
        username=request.POST.def get_context_data(self, **kwargs) -> dict[str, Any]:
            context = super().get_context_data(**kwargs)
            context[""] = 
            return context
        
        city=request.POST.get("city")
        ProfilePicture=request.FILES.get("image")
        dob=request.POST.get("dob")
        
        if ProfilePicture:
            profile.profilePicture=ProfilePicture
        profile.dateOfBirth=dob
        profile.city=city
        profile.save()
        return  redirect("profile",pk=profile.id)
    content={"profile":profile}
    return render(request,"accounts/update_profile.html",content)
