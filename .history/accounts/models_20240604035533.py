from django.db import models

from django.contrib.auth.models import User


class USerProfile(models.Model):
    profileName=models.CharField() 