from django.shortcuts import render,redirect
from .form import restaurant_form
from django.contrib.auth.models import User
from .models import restaurants,hotel,dish
from django.contrib.auth import login ,authenticate,logout
from  django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def home(request):
    q=request.POST.get("q") if request.POST.get("q") != None else ''
    users=User.objects.all()
    restaurant=restaurants.objects.all()
    # dishes=restaurants.dishes.all()
    content={"users":users,"restaurants":restaurant,"dish":dish}
    return render(request,"home.html",content)

def login_page(request):
    page="login"
    username=request.POST.get("username")
    password=request.POST.get("password")
    if request.method == "POST":
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,"incorect username")
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect("home")
        else :
            messages.error(request,"incorect username and password ")
    context={"page":page}
    return render(request,"login_page.html",context)
def register(request):
    page="resister"
    if request.method =="POST":
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=User.objects.create(
            first_name=firstname,
            last_name=lastname,
            username=username
            )
        
        user.set_password(password)
        user.save()
        login(request,user)
        return redirect("home")
    context={"page":page}
    return render(request,"login_page.html",context)
@login_required(login_url="login-page")
def logout_page(request):
    logout(request)
    return redirect("login-page")


@login_required(login_url="login-page ")
def create_restaurant(request):
    form=restaurant_form()
    if request.method == "POST":
        form=restaurant_form(request.POST)
        if form.is_valid():
            forms=form.save(commit=False)
            forms.user=request.user
            forms.save()
            return redirect("home")
    content={"form":form}
    return render(request,"restaurantform.html",content)
@login_required(login_url="login-page")
def update_restaurant(request,pk):
    restaurant_obj=restaurants.objects.get(id=pk)
    form=restaurant_form(instance=restaurant_obj)
    if request.method == "POST":
        form=restaurant_form(request.POST,instance=restaurant_obj)
        if form.is_valid():
            restaurant_obj.save()
            return redirect("home")
    content={"form":form}
    return render(request,"restaurantform.html",content)
@login_required(login_url="login-page")
def delete_restaurant(request,pk):
    restaurant_obj=restaurants.objects.get(id=pk)
    if request.method == "POST":
        restaurant_obj.delete()
        return redirect("home")
    content={"obj":restaurant_obj}
    return render(request,"delete_restaurant.html",content)
def restaurant_data(request,pk):
    restaurant=restaurants.objects.get(id=pk)
    dishes=restaurant.dish_set.all()
    if request.method == "POST":
        create_dishes=dish.objects.create(
            dishName=request.POST.get("dishname"),
            description=request.POST.get("description"),
            dishImage=request.POST.get("dishImage"),
            user=request.user,
            hotel=restaurant.hotel,
            restaurants=restaurant
            )
        return redirect("restaurant-data",pk=restaurant.id)
    
    if request.POST.get("search_dish"):
        dishes=dishes.filter(Q(description__icontains=request.POST.get("search_dish")) |
                             Q(dishName__icontains=request.POST.get("search_dish"))                              
                             )
        print("dish is",dishes)    

    content={"restaurant":restaurant,"dishes":dishes}
    return render(request,"restaurand_data.html",content)
@login_required(login_url="login-page")
def delete_dish(request,pk):
    dish_obj=dish.objects.get(id=pk)
    restaurant=dish_obj.restaurants
    dish_obj.delete()
    return redirect("restaurant-data",pk=restaurant.id)
    



def update_dish(request,pk):
    dish_obj=dish.objects.get(id=pk)
    dishname=request.POST.get("dishname")
    dish_derscription=request.POST.get("description")
    dishimage= request.POST.get("dishImage")
    if request.method == "POST":
        dish_obj.dishName=dishname
        dish_obj.description=dish_derscription
        dish_obj.dishImage=dishimage
        dish_obj.save()
        return redirect("restaurant-data",pk=dish_obj.restaurants.id)
    return render(request,"update_dish.html")