from celery import shared_task

@shared_task(bind=True)
def fun1(self):
            register_user_to_send_mail([email],fullname)

    return "DONE"
