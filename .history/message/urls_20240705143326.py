from django.urls import path 
from . import views
urlpatterns = [
    path("<str:rest_id>/<str:rest_id>/",views.message_home,name="message-home"),
    path("message-list/<str:id>/",views.all_reciever_message,name="message-list"),

]
