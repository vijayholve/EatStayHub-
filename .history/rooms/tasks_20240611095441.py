from .models import Room, Booking   
from .seed import send_mail_to_user_after_booking
from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task()
def send_mail_booking_task(self,receiver_mail, room_id, booking_id):
    try:
        logger.info(f"Sending email to {receiver_mail} for room {room_id} and booking {booking_id}")
        send_mail_to_user_after_booking(receiver_mail, room_id, booking_id)
        logger.info("Email sending task done")
        return "DONE"
    except Room.DoesNotExist:
        print("Room not found")
        return "Failed: Room not found."
    except Booking.DoesNotExist:
        print("Booking not found")
        return "Failed: Booking not found."
    except Exception as e:
        print(f"Error: {e}")
        return f"Failed: {e}"