from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import restaurants,dish
from .serializable import serializer_restaurant,serializer_dish,User_Serializar
from django.contrib.auth.models import User
@api_view(["GET"])
def all_api(request):
    content={
        "api/restaurants":"all_restaurants", 
        "api/restaurants/id":"specific_restaurants",
        "api/dishes":"all_dishes",
        "api/dishes/id":"specific_dishes",
        "api/user":"all_User"
    }
    return Response(content)    

@api_view(["GET","POST"])
def restaurants_api(request):
    if request.method == "GET":
        restaurant=restaurants.objects.all()
        serialzer=serializer_restaurant(restaurant,many=True)
        return Response(serialzer.data)
    elif request.method == "POST":
        data=request.data
        serialzer=serializer_restaurant(data=data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        return Response(serialzer.errors)
    
        
@api_view(["GET"])
def restaurant_api(request,pk):
    restaurant=restaurants.objects.get(id=pk)
    serialzer=serializer_restaurant(restaurant,many=False)
    return Response(serialzer.data)

@api_view(["GET","POST","PUT"])
def dishes_api(request):
    if request.method == "GET":
        dishes=dish.objects.all()
        serializer=serializer_dish(dishes,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data=request.data 
        serializer=serializer_dish(data=data)
        if serializer.is_valid():
            serializer.save()
            Response(serializer.data)
    elif request.method == "PUT":
        data=request.data
        obj=dish.objects.get(id=request.data["id"])
        serializer=serializer_dish(obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "PATCH":
        data=request.data 
        obj=dish.objects.get(id=request.data["id"])
        serializer=serializer_dish(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.
        
         
@api_view(["GET"])
def dish_api(request,pk):
    
    dishes=dish.objects.get(id=pk)
    serialzer=serializer_dish(dishes,many=False)
    return Response(serialzer.data)
@api_view(['GET','POST','PUT','PATCH'])
def User_api(request):
    if request.method == "GET":
        print("method is Post ")
        users=User.objects.all()
        serializer=User_Serializar(users,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = User_Serializar(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data)
            except:
                return Response({'error': 'Username already exists'})
        return Response(serializer.errors)
    if request.method == "PUT":
        obj=User.objects.get(id=request.data["id"])
        data=request.data 
        serializer=User_Serializar(obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "PATCH":
        obj=User.objects.get(id=request.data['id'])
        data=request.data
        serializer=User_Serializar(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        

    