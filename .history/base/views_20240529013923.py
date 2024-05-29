from django.shortcuts import render,redirect
from .form import restaurant_form
from django.contrib.auth.models import User
from .models import restaurants,hotel,dish
from django.contrib.auth import login ,authenticate,logout
from  django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import aggregates
from .seed import register_user_to_send_mail
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
        except Exception as e:
            messages.error(request,f"error is {e}")
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
        return _extracted_from_register_4(request)
    context={"page":page}
    return render(request,"login_page.html",context)


# TODO Rename this here and in `register`
def _extracted_from_register_4(request):
    fullname=request.POST.get("fullname")
    email=request.POST.get("email")
    username=request.POST.get("username")
    password=request.POST.get("password")
    confirm_password=request.POST.get("confirm-password")
    print(fullname,"n",email,"/n",username,"/n",password,"/n",confirm_password)
    if password != confirm_password :
        messages.error(request,"Password Does Not Matching")
        return redirect("register")
    if username is None or len(username) <=5 :
        messages.error(request,"please enter username")
        return redirect("register")

    if fullname is None or len(fullname) <= 5:
        messages.error(request,"please enter fullname")
        return redirect("register")

    if email is None or len(email) <= 5:
        messages.error(request,"please enter email")
        return redirect("register")
    try:

        user=User.objects.create(
            first_name=fullname,
            email=email,
            username=username
            )
    except Exception as e:
        messages.error(request,"error is :e ")
    user.set_password(password)
    user.save()
    login(request,user)
    register_user_to_send_mail([email],fullname)
        # register_user_to_send_mail(["vijucode@gmail.com"],"vijay")

    return redirect("home")
@login_required(login_url="login-page")
def logout_page(request):
    logout(request)
    return redirect("login-page")
@login_required(login_url="login-page ")
def create_restaurant(request):
    hotel_obj=hotel.objects.get(id=1)
    # form=restaurant_form()
    if request.method == "POST":
        restaurantName=request.POST.get("restaurantName")
        locations=request.POST.get("locations")
        restaurant_obj=restaurants.objects.create(
            restaurantName=restaurantName,
            locations=locations,
           hotel=hotel_obj,
           user=request.user
        )
        
        restaurant_obj.save()
        return redirect("home")
    # content={"form":form}
    return render(request,"restaurantform.html")
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
    q= request.GET.get("q")
    dishes=restaurant.dish_set.all()
    create_dish(request,restaurant.id)
    if q is not None :
         
        dishes=dishes.filter(Q(dishName__icontains=q) |
                             Q(description__icontains=q) |
                             Q(price__icontains=q) 
                             )
   
       

    content={"restaurant":restaurant,"dishes":dishes}
    return render(request,"restaurant_data.html",content)
@login_required(login_url="login-page")
def delete_dish(request,pk):
    dish_obj=dish.objects.get(id=pk)
    restaurant=dish_obj.restaurants
    dish_obj.delete()
    return redirect("restaurant-data",pk=restaurant.id)
@login_required(login_url="login-page")
def update_dish(request,pk):
    dish_obj=dish.objects.get(id=pk)
    dishname=request.POST.get("dishname")
    dish_derscription=request.POST.get("description")
    dishimage= request.POST.get("dishImage")  
    price= request.POST.get("price")
    restaurant=dish.res
    if request.method == "POST":
        dish_obj.dishName=dishname
        dish_obj.description=dish_derscription
        dish_obj.dishImage=dishimage
        dish_obj.price = price
        dish_obj.save()
        return redirect("restaurant-data",pk=dish_obj.restaurants.id)
    return render(request,"update_dish.html")

# def blank(request):
#     # form=user_form()
#     context={"form":form}
#     return render(request,"blank_form.html",context)

def create_dish(request,pk):
    restaurant=restaurants.objects.get(id=pk)
    if request.method == "POST":
        try:
            
            create_dishes=dish.objects.create(
                    dishName=request.POST.get("dishname"),
                    description=request.POST.get("description"),
                    dishImage=request.POST.get("dishImage"),
                    user=request.user,
                    hotel=restaurant.hotel,
                    restaurants=restaurant,
                    price=request.POST.get("price"),
                    ) 
        except Exception as e:
            messages.error(request,e)
        return redirect("restaurant-data",pk=restaurant.id)
    content={"restaurant":restaurant}    
    return render(request,'dishform.html',content   )
    
