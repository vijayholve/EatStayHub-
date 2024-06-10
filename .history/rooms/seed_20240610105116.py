from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from .models import Room,Booking

def send_mail_to_user_after_booking(receiver_mail,roomNo):
    Subject=f" Your Upcoming Stay at [Hotel Name} – All You Need to Know! 🌟
    



