from django.db import models

from django.contrib.auth.models import User


class USerProfile(models.Model):
    profileName=Modle.models.CharField(_(""), max_length=50) 