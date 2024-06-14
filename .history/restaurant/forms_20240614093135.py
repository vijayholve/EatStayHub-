from django.forms import ModelForm
from base.models import restaurants


class restaurant_form(ModelForm):
    class Meta:
        model=restaurants
        fields="__all__"
        exclude=["user"]  
        
class many_images(class FormName(forms.ModelForm):
    class Meta:
        model = ModelName
        fields = [Model Fields])