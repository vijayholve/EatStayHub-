from django.forms import ModelForm
from base.models import restaurants,Images


class restaurant_form(ModelForm):
    class Meta:
        model=restaurants
        fields="__all__"
        exclude=["user"]  
        
class many_images(Modelform):
    class Mata:
        model=Images
        fields=["image"]