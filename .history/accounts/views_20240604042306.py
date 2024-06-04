from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import USerProfile

def profile(request):
    userProfile=USerProfile.objects.all()
    content={"userProfile":pro}
    return render(request,"userProfile.html")