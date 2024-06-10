from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import UserProfile
from rooms.models import Room,Booking
def User_profile_fun(request,pk):
    user=User.objects.get(id=pk)
    restaurant=user.restaurants_set.all()
    booked=user.booking_set.all()
    rooms=user.objects.all()
    if user.userprofile:
        profile=user.userprofile
    content={"user":user,"profile":profile,"restaurant":restaurant}
    return render(request,"accounts/userProfile.html",content)
def update_profile(request,pk):
    profile=UserProfile.objects.get(id=pk)
    if request.method == "POST":
        
        return _extracted_from_update_profile_5(request, profile)
    content={"profile":profile}
    return render(request,"accounts/update_profile.html",content)


# TODO Rename this here and in `update_profile`
def _extracted_from_update_profile_5(request, profile):
    username=request.POST.get("username")
    city=request.POST.get("city")
    ProfilePicture=request.FILES.get("image")
    dob=request.POST.get("dob")

    if ProfilePicture:
        profile.profilePicture=ProfilePicture
    if dob:
        profile.dateOfBirth=dob
    profile.city=city
    profile.user.username=username
    profile.save()
    return  redirect("profile",pk=profile.user.id)

def create_profile(request):
    users=User.objects.all()
    if request.method == "POST":
        return _extracted_from_create_profile_6(request, users)
    content={"users":users}
    return render(request,"accounts/createprofile.html",content)    
def _extracted_from_create_profile_6(request,users):
    
    city=request.POST.get("city")
    ProfilePicture=request.FILES.get("image")
    dob=request.POST.get("dob")
    user=request.user
    profile, created = UserProfile.objects.get_or_create(user=user)
    profile.profilePicture = ProfilePicture
    profile.dateOfBirth = dob
    profile.city = city
    profile.save()
    # if ProfilePicture:
    #     profile.profilePicture=ProfilePicture
    # if dob:
    #     profile.dateOfBirth=dob
    # profile.city=city
    # user=request.user
    profile.save()
    return  redirect("profile",pk=profile.user.id)