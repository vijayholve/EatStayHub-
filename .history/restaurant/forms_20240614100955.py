from django.forms import ModelForm,FileInput,ClearableFileInput
from base.models import restaurants,Images


class restaurant_form(ModelForm):
    class Meta:
        model=restaurants
        fields="__all__"
        exclude=["user"]  
        
class many_images_form(ModelForm):
    class Mata:
        model=Images
        fields=["image"]
        widgets = {
            'image':FileInput(),
        }
image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
