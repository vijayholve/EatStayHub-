from rest_frameworkim
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

        
class serializer_dish(ModelSerializer):
    # user=User_Serializar()
    class Meta:
        model=dish
        fields=["id","dishName","price"]
    def validate_price(self,price):# as you can in the function after the validate add _ and add the column(price) that acces it
        if price < 100:
            raise ValidationError("Price should be gretter than 100")
        return price
        
    def validate(self,data):
        speacial="!@#$%^&*()_?"
        if any( c in speacial for c in data["dishName"]):
            raise ValidationError("speacial character Not allowed")
        
        return data
        
             
       
