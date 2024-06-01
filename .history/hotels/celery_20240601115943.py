from __future__ import absolute_import,unicode_literals
import os
from celery import Celery   

from django.conf import settings

os.environ.setdefault("DJANGO_SETTING_MODULE','hotels.settings')('DJANGO_SETTINGS_MODULE', 'hotels.settings')
app=Celery("hotels")
app.conf.enable_utc=False
app.conf.update(timezone="Asia/kolkata")
app.config_from_object(settings,namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def bind_fun(self):
    print(f"request : {self.request!r} ")