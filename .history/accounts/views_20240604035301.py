from django.shortcuts import render
from django.contrib.auth.models import User


class UserProfile(models.Model):
    ProfileNAme=class MODELNAME(models.Model):
        """Model definition for MODELNAME."""
    
        # TODO: Define fields here
    
        class Meta:
            """Meta definition for MODELNAME."""
    
            verbose_name = 'MODELNAME'
            verbose_name_plural = 'MODELNAMEs'
    
        def __str__(self):
            """Unicode representation of MODELNAME."""
            pass
    