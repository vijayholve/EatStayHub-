from __future__ import absolute_import,unicode_literals
import os
from celery import Celery  
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','hotels.settings')
app=Celery("hotels")
app.conf.enable_utc=False
app.conf.update(timezone="Asia/Kolkata")
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def bind_fun(self):
    print(f"request : {self.request!r} ")