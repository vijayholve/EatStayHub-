from django.urls import path,include
from . import views
urlpatterns = [
    path("<str:>",views.profile,name="profile"),
]
