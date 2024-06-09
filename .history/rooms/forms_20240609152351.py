from django.forms import ModelForm
from .models import Room

class room_form(ModelForm):
    class Meta:
        model=Room
        fields="__all__"
        exclude=["user","hotels"]

class booking_room_form(ModelForm):
    class Meta:
        class ModelName(models.Model):
        
            def __str__(self):
                pass
        
            class Meta:
                db_table = ''
                managed = True
                verbose_name = 'ModelName'
                verbose_name_plural = 'ModelNames'







