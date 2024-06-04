from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    =models.OneToOneField(User,on_delete=models.CASCADE)
    profilePicture=models.ImageField(upload_to="accouts/",default=rf"image\profile\userprofile.jpg",null=True,blank=True)
    dateOfBirth=models.DateField(null=True,blank=True)
    city=models.CharField(default=True,max_length=200,null=True,blank=True)
    def __str__(self) -> str:
        return self.profileName.username
    
    
    
     