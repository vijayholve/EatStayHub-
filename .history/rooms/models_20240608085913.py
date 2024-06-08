from django.db import models
from django.contrib.auth.models import User
from base.models import hotel
import uuid
class Room(models.Model):
    roomNo=models.UUIDField(primary_key=True,default=uuid.uuid4)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    roomName=models.CharField(max_length=100)
    roomType=models.CharField(max_length=100)
    price=models.IntegerField()
    roomImage=models.ImageField(upload_to="roomImages",null=True,blank=True)
    def __str__(self) -> str:
        return self.roomName