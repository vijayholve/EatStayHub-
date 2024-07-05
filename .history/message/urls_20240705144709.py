from django.urls import path 
from . import views
urlpatterns = [
    path("<str:rest_id>/<str:user_id>/",views.message_home,name="message-home"),

]
