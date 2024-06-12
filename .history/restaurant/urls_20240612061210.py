from django.urls import path
from . import views
urlpatterns = [
path("",views.restaurant_data,name="restaurant-data"),
path("restaurant-update/<str:pk>/",views.update_restaurant,name="restaurant-update"),
path("restaurant-delete/<str:pk>/",views.delete_restaurant,name="restaurant-delete"),
path("dish-create/<str:pk>/",views.create_dish,name="dish-create"), 
path("dish-delete/<str:pk>/",views.delete_dish,name="dish-delete"),
path("dish-update/<str:pk>/",views.update_dish,name="dish-update"), 
path("dish-order/<str:pk>/",views.order_dish,name="dish-order"),
]




