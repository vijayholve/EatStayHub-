from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from .models import Room,Booking

def send_mail_to_user_after_booking(receiver_mail,room,booked):
    
    Subject=f" Your Upcoming Stay at {room.roomName}– All You Need to Know! 🌟"
    content=f"""Dear [Guest's Name],

Greetings from [{room.user.username}]!

We are delighted to confirm your booking and can't wait to welcome you to our beautiful property. Your upcoming stay promises to be a memorable one, and we are here to ensure every detail is perfect.
    
       
🛏️ Your Room Details:
Room Type: [Room Type]
Check-in Date: {booked.start_date}
Check-out Date: {booked.end_date}
duration : {booked.duration}
Total Cost: {booked.total_price}



📍 Location:
Our hotel is conveniently located at [Hotel Address]. Whether you're here for business or leisure, you'll find our central location ideal for exploring the vibrant surroundings.

🕒 Check-in & Check-out:
Check-in Time: From 3:00 PM
Check-out Time: By 11:00 AM

We look forward to providing you with an exceptional stay. Thank you for choosing [Hotel Name]. Safe travels, and see you soon!

Warm Regards,

[Vijay Gholve]
[Your Position]


""" 
    try:
        sender=settings.EMAIL_HOST_USER
        send_mail(Subject,content,sender,receiver_mail)
    except Exception as e:
        print(e)
    
    



