from django.urls import path 
from . import views
urlpatterns = [
    path("<str:rest_id>/",views.message_home,name="message-home"),
    path("receiver-list/<str:rest_id>/",views.receiver_list,name="receiver-list"),
    path("owner/<str:receiver_id>/<str:sender_id>/",views.restaurant_owner_reply,
         name="message-owner"),
]
