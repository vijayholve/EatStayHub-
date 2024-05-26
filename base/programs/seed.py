from faker import Faker
import random
from base.models import restaurants,hotel
from django.contrib.auth.models import User
from .data import indian_dishes
hotel_obj=hotel.objects.get(id=1)
user=User.objects.all()
user_list=list(user)
def seed_fun(n):
    for _ in range(n):
        fake=Faker()
        restaurantName1=fake.name()
        location=fake.address()
        restaurant=restaurants.objects.create(
                restaurantName=restaurantName1,
                locations=location,
                hotel=hotel_obj,
                user=random.choice(user_list)
        )
        
def seed_dish_restarants_create():
    restaurant=restaurants.objects.all()
    for rest in restaurant:
        for indDish in indian_dishes:
            fake=Faker()
            description = fake.paragraph(nb_sentences=3)  
            dish=rest.dish_set.create(
                dishName=indDish,
                description=description,
                price=random.randint(100,999),
                restaurants=rest,
                user=random.choice(user_list),
                hotel=hotel_obj            
            )
def seed_restaurants_dish_delete():
    restaurant=restaurants.objects.all()
    for rest in restaurant:
        for dish in rest.dish_set.all():
            dish.delete()
            
def seed_dish_restarant_create(restaurant):
    for indDish in indian_dishes:
        fake=Faker()
        description = fake.paragraph(nb_sentences=3)  
        dish=restaurant.dish_set.create(
            dishName=indDish,
            description=description,
            price=random.randint(100,999),
            restaurants=restaurant,
            user=random.choice(user_list),
            hotel=hotel_obj            
        )
def seed_restaurant_dish_delete(restaurant):
    for dish in restaurant.dish_set.all():
        dish.delete()