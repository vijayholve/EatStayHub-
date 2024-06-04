from django.db import models

from django.contrib.auth.models import User


class USerProfile(models.Model):
    profileName=Model.fieldName = models.CharField(max_length = 150)
     