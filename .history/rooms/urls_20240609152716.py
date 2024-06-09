from django.urls import path
from . import views

urlpatterns = [
    path("",views.home_room,name="home-room"),
    path("create-room/",views.create_room,name="create-room"),
    path("delete-room/<str:pk>/",views.delete_room,name="delete-room"),
    path()

]



