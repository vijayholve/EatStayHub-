from django.core.mail import send_mail
from django.conf import settings
from .models import Room, Booking

def send_mail_to_user_after_booking( pk, id):
    room = Room.objects.get(id=pk)
    booking = Booking.objects.get(id=id)
    
    user = booking.user
    subject = f"Your Upcoming Stay at {room.roomName}– All You Need to Know! 🌟"
    content = f"""Dear {user},

        We are delighted to confirm your booking and can't wait to welcome you to our beautiful property. Your upcoming stay promises to be a memorable one, and we are here to ensure every detail is perfect.
            
        🛏️ Your Room Details:
        Room Type: {room.roomType}
        Check-in Date: {booking.start_date}
        Check-out Date: {booking.end_date}
        Duration: {booking.duration}
        Total Cost: {booking.total_price}

        📍 Location:
        Our hotel is conveniently located at [Hotel Address]. Whether you're here for business or leisure, you'll find our central location ideal for exploring the vibrant surroundings.

        🕒 Check-in & Check-out:
        Check-in Time: From 3:00 PM
        Check-out Time: By 11:00 AM

        We look forward to providing you with an exceptional stay. Thank you for choosing [Hotel Name]. Safe travels, and see you soon!

        Warm Regards,

        Vijay Gholve
        Manager
        Hotel VJ
        vijaygholve77v@gmail.com
        8080028963
        kharadi
        Pune 14 [411014]
        """
    try:
        sender = settings.EMAIL_HOST_USER
        receiver_mail=booking.user.email
        send_mail(subject, content, sender, [receiver_mail])
        print("Email sent")
    except Exception as e:
        print(e)
def delete_booking():
    booking=Booking.objects.all()
    booking.delete()
    return "DOne"