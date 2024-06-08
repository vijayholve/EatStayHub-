from django.forms import ModelForm
from .models import Room

class room_form(ModelForm):
    class Meta:
        model=Room
        fields="__all__"
        exclude=[""]









