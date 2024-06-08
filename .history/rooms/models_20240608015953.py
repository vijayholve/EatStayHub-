from django.db import models

# Create your models here.
class room(models.Model):
    roomName=models.CharField(max_length=100)
    roomType=models.CharField(max_length=100)
    price=models.IntegerField()
    roomImage=