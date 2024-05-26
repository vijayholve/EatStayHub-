from django.forms import ModelForm
from .models import restaurants
from django.contrib.auth.models import User

class restaurant_form(ModelForm):
    class Meta:
        model=restaurants
        fields="__all__"
        exclude=["user"]    
class user_form(ModelForm):
    class Meta:
        model=User
        fields="__all__"
