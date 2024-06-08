from django.urls import path
from . import views

urlpatterns = [
    path("",views.horoom,name="home-room"),
    path("create-room",views.create_room,name="create-room"),
]



