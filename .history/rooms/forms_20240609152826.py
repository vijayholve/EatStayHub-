from django.forms import ModelForm
from .models import Room,Booking

class room_form(ModelForm):
    class Meta:
        model=Room
        fields="__all__"
        exclude=["user","hotels"]

class booking_room_form(ModelForm):
    class Meta:
        model=Booking
        field="__all__"
         = ModelName.objects.exclude(PassArguments)
        







