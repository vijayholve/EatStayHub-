from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotels.settings')

app = Celery("hotels")
app.conf.enable_utc=False

app.conf.updtae(timezone="Asia/Kolkata")
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule={
    'send-meail-everyday-at-1pm':{
        'task':'base.tasks.send_mail_task',
        'schedule':
    }
}
@app.task(bind=True)
def bind_fun(self):
    print(f"request : {self.request!r}")
