from celery import shared_task
from .
from .seed import send_mail_to_user_after_booking@shared_task
def send_mail__booking_task(receiver_mail, room_id, booking_id):
    try:
        room = Room.objects.get(id=room_id)
        booking = Booking.objects.get(id=booking_id)
        send_mail_to_user_after_booking(receiver_mail, room, booking)
        return "DONE"
    except Room.DoesNotExist or Booking.DoesNotExist:
        return "Failed: Room or Booking not found."

    




