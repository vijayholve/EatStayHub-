from celery import shared_task
from .seed import send_mail_to_user_after_booking
@shared_task(bind=True)
def send_mail__booking_task(receiver_mail, room, book):
    send_mail_to_user_after_booking(receiver_mail, room, book)
    return "DONE"
    




