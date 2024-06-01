from __future__ import absolute_import,unicode_literals
import os
from celery import Celery

from django.conf import settings

os.environ.setdefault("DJANGO_SETTING_MODULE","hotels.settings")
app=Celery("hotels")
app.conf.enable_utc=False
app.conf.up