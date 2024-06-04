from django.shortcuts import render
from django.contrib.auth.models import User


class UserProfile(models.Models):
    user=models.OneToOneField(User,on_delete=models.CASCADE)