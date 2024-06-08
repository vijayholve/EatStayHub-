from rest_framework.serializers import ModelSerializer
from base.models import restaurants,dish
from django.contrib.auth.models import User
class serializer_restaurant(ModelSerializer):
    class Meta:
        model=restaurants
        fields="__all__"
        # depth=1
class User_Serializar(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'password', 'email']
    \
        
class serializer_dish(ModelSerializer):
    user=User_Serializar()
    class Meta:
        model=dish
        fields="__all__"
    
    def valid
        
