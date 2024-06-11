from django.db import models
from django.contrib.auth.models import User
class hotel(models.Model):
    name=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class restaurants(models.Model):
    restaurantName=models.CharField(max_length=200)
    locations=models.CharField(max_length=200)
    image=models.FileField(upload_to="restaurant_images",null="True",blank=True)
    hotel=models.ForeignKey(hotel,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.restaurantName
    class Meta:
        ordering=["-id"]
class dish(models.Model):
    dishName=models.CharField(max_length=200)
    description=models.CharField( max_length=200)
    price=models.IntegerField(blank=True,null=True)
    restaurants=models.ForeignKey(restaurants,on_delete=models.SET_NULL,null=True,blank= True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="dishes")
    dishImage=models.FileField(upload_to="images/",max_length=250,null=True,blank=True)
    hotel=models.ForeignKey(hotel,on_delete=models.CASCADE)
    def __str__(self):
        return self.dishName
class orders(models.Model):
    restaurants=models.ForeignKey(restaurants,on_delete=models.CASCADE)
    dish=models.OneToOneField(dish,on_delete=models.SET_NULL,related_name="dish")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    delivery_charges=models.IntegerField(default=50)
    total_charges=models.IntegerField()
    def def __str__(self):
        return f"{restaurants.restName}"