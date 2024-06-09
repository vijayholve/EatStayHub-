from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.api_login, name='api-login'),
    path('restaurants/', views.api_restaurants, name='restaurants-api'),
    path('restaurants/<str:pk>/', views.api_restaurant_detail, name='restaurant-api'),
    path('dishes/', views.api_dishes, name='dishes-api'),
    path('dishes/<str:pk>/', views.api_dish_detail, name='dish-api'),
    path('user/', views.api_user, name='user-api'),
]
