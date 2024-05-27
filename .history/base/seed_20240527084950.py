from faker import Faker
import random
from .models import restaurants,hotel
from django.contrib.auth.models import User
from .data import indian_dishes
from django.conf import settings
from django.core.mail import send_mail
from .models import hotel
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
        
def seed_dish():
    restaurant=restaurants.objects.all()
    for rest in restaurant:
        for indDish in indian_dishes:
            fake=Faker()
            description = fake.paragraph(nb_sentences=3)  # Generate a paragraph with 3 sentences
         
            dish=rest.dish_set.create(
                dishName=indDish,
                description=description,
                price=random.randint(100,999),
                restaurants=rest,
                user=random.choice(user_list),
                hotel=hotel_obj            
            )
def seed_dish_delete():
    restaurant=restaurants.objects.all()
    for rest in restaurant:
        for dish in rest.dish_set.all():
            dish.delete()
            
def register_user_to_send_mail(receiver_email,fullname):
    hotel_obj=hotel.objects.get(id=1)
    hotel_name=hotel_obj.name
    subject=f"Welcome to {hotel_name} – Your Account is Ready!"
    email_content = f"""
Subject: Welcome to {hotel_name} – Your Account is Ready!

Dear {user_name},

Thank you for creating an account with {hotel_name}! We're thrilled to have you join our community.

Explore our website to discover a variety of delicious dishes crafted by our expert chefs. Whether you crave savory, sweet, or anything in between, we have something to satisfy every palate.

Visit us at {vj} and start your culinary adventure today!

Bon appétit!

Best regards,
Vijay Gholve
{hotel_name} Team
"""