from celery import shared_task
from .models import Room,Booking
from .seed import send_mail_to_user_after_booking
@shared_task
def send_mail_booking_task(sereceiver_mail, room_id, booking_id):
    try:
        room = Room.objects.get(id=room_id)
        booking = Booking.objects.get(id=booking_id)
        send_mail_to_user_after_booking(receiver_mail, room, booking)
        print("done")
        return "DONE"
    except Room.DoesNotExist or Booking.DoesNotExist:
        "error"
        return "Failed: Room or Booking not found."

    




