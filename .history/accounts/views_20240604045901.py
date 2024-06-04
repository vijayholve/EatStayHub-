from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import USerProfile

def profile(request,pk):
    user=User.objects.get(id=pk)
    
    content={"userProfile":user}
    return render(request,"accounts/userProfile.html",content)