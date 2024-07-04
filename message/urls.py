from django.urls import path 
from . import views
urlpatterns = [
    path("<str:pk>/",views.message_home,name="message-home"),
]
