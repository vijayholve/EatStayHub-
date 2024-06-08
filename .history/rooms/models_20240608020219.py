from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class room(models.Model):
    hotels=mdoe
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    roomName=models.CharField(max_length=100)
    roomType=models.CharField(max_length=100)
    price=models.IntegerField()
    roomImage=models.ImageField(upload_to="roomimages")