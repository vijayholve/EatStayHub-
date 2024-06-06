from rest_framework.serializers import ModelSerializer
from base.models import restaurants,dish
from django.contrib.auth.models import User
class serializer_restaurant(ModelSerializer):
    class Meta:
        model=restaurants
        fields="__all__"
class serializer_dish(ModelSerializer):
    class Meta:
        model=dish
        fields="__all__"

    
class all_Data_Serializar(ModelSerializer):
    class Meta:
        model=User
        field=['username']