from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.User_profile_fun,name="profile"),
    path("profile-update/",views.update_profile,name="profile-update"),
]
