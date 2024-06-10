from celery import shared_task
from .models import Room,Booking
from .seed import send_mail_to_user_after_booking
@shared_task
def send_mail_booking_task(receiver_mail, room_id, booking_id):
    try:
        
        send_mail_to_user_after_booking(receiver_mail, room_id, booking_id)
        print("done")
        return "DONE"
    except Room.DoesNotExist or Booking.DoesNotExist:
        "error"
        return "Failed: Room or Booking not found."

    




