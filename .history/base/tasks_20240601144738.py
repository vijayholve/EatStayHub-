from celery import shared_task
from .seed import register_user_to_send_mail
import time
@shared_task(bind=True)
def fun1(self,email,fullname):
    register_user_to_send_mail([email],fullname)
    
    return time.strftime("%m")
