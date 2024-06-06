from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import restaurants,dish
from .serializable import serializer_restaurant,serializer_dish,User_Serializar
from django.contrib.auth.models import User
@api_view(["GET"])
def all_api(request):
    return Response({"name":"vijay"})

@api_view(["GET"])
def restaurants_api(request):
    restaurant=restaurants.objects.all()
    serialzer=serializer_restaurant(restaurant,many=True)
    return Response(serialzer.data) 
@api_view(["GET"])
def restaurant_api(request,pk):
    restaurant=restaurants.objects.get(id=pk)
    serialzer=serializer_restaurant(restaurant,many=False)
    return Response(serialzer.data)

@api_view(["GET"])
def dishes_api(request):
    dishes=dish.objects.all()
    serializer=serializer_dish(dishes,many=True)
    return Response(serializer.data)
@api_view(["GET"])
def dish_api(request,pk):
    dishes=dish.objects.get(id=pk)
    serialzer=serializer_dish(dishes,many=False)
    return Response(serialzer.data)

    
    
    
    
@api_view(['GET',"POST"])
def all_data_api(request):
    users=User.objects.all()
    serializer=User_Serializar(users,many=True)
    return Response(ser)