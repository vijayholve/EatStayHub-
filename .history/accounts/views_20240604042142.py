from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse


def profile(request):
    
    return render(request,"userProfile.html")