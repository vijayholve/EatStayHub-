from django.db import models

from django.contrib.auth.models import User


class USerProfile(models.Model):
    profileName=models.OneToOneField(User,on_delete=models.CASCADE)
    profilePicture=models.ImageField(upload_to="accout/")
     