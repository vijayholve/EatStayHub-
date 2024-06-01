from celery import shared_task
from .seed import reg
@shared_task(bind=True)
def fun1(self):
    
    return "DONE"
