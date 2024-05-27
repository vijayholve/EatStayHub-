from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
  
urlpatterns = [
path("",views.home,name="home"),
path("login-page",views.login_page,name="login-page"),
path("logout-page",views.logout_page,name="logout-page"),    
path("register",views.register,name="register"),
path("restaurant-create/",views.create_restaurant,name="restaurant-create"),
path("restaurant-data/<str:pk>/",views.restaurant_data,name="restaurant-data"),
path("restaurant-update/<str:pk>/",views.update_restaurant,name="restaurant-update"),
path("restaurant-delete/<str:pk>/",views.delete_restaurant,name="restaurant-delete"),


path("dish-delete/<str:pk>/",views.delete_dish,name="dish-delete"),


]
