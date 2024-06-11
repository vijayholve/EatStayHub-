from celery import shared_task
from .models import Room, Booking
from .seed import send_mail_to_user_after_booking

@shared_task(bind=True)
def send_mail_booking_task(receiver_mail, room_id, booking_id):
    try:
        send_mail_to_user_after_booking.delay(receiver_mail, room_id, booking_id)
        print("Email sending task done")
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
