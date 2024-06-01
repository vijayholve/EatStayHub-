from celery import shared_task
from .seed import register_user_to_send_mail
import datetime
@shared_task(bind=True)
def fun1(self,email,fullname):
    register_user_to_send_mail([email],fullname)
    times=datetime.now()
    current_time = times.strftime("%Y-%m-%d %H:%M:%S")

    return f"{current_time} uploaded "
