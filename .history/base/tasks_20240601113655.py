from celery import shared_task

@shared_task(bind=True)
def fun1(self):
    return "DONE"