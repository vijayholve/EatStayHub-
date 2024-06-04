from django.db import models

from django.contrib.auth.models import User


class USerProfile(models.Model):
    profileName=models.fieldName = models.OneToOneField(RelatedModel, on_delete=models.CASCADE)
    (max_length=200)
     