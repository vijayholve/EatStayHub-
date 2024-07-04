from django.urls import path 
from . import views
urlpatterns = [
    path("<str:rest_id>/<str:",views.message_home,name="message-home"),
]
