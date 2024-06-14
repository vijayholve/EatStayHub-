from django.forms import ModelForm,ClearableFileInput
from base.models import restaurants,Images


class restaurant_form(ModelForm):
    class Meta:
        model=restaurants
        fields="__all__"
        exclude=["user"]  
        
class many_images(ModelForm):
    class Mata:
        model=Images
        fields=["image"]
        widgets = {
            'image': ClearableFileInput(attrs={'multiple': True}),
        }