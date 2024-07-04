from django.urls import path 
from . import views
urlpatterns = [
    path("<str:rest_id>/<tsr",views.message_home,name="message-home"),
]
