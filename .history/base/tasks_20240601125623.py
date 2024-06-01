from celery import shared

@shared_task(bind=True)
def fun1(self):
    for i in range(1,10):
        print(i)
    return "DONE"