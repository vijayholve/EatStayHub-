from django.db import models
from django.contrib.auth.models import User0class hotel(models.Model):
    name=models.CharField(max_length=200)
    city=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class restaurants(models.Model):
    restaurantName=models.CharField(max_length=20)
    locations=models.CharField(max_length=20)
    image=models.FileField(upload_to="restaurant_images",null="True",blank=True)
    hotel=models.ForeignKey(hotel,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.restaurantName
    class Meta:
        ordering=["-id"]
class dish(models.Model):
    dishName=models.CharField(max_length=20)
    description=models.CharField( max_length=20)
    price=models.IntegerField(blank=True,null=True)
    restaurants=models.ForeignKey(restaurants,on_delete=models.SET_NULL,null=True,blank= True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="dishes")
    dishImage=models.FileField(upload_to="images/",max_length=250,null=True,blank=True)
    hotel=models.ForeignKey(hotel,on_delete=models.CASCADE)
    def __str__(self):
        return self.dishName