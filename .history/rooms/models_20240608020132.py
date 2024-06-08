from django.db import models
from django.contrib.auth.models import 
# Create your models here.
class room(models.Model):
    user=models.ForeignKey()
    roomName=models.CharField(max_length=100)
    roomType=models.CharField(max_length=100)
    price=models.IntegerField()
    roomImage=models.ImageField(upload_to="roomimages")