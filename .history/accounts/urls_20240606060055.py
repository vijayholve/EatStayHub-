from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.profile,name="profile"),
    path("profile-update",views.update_profile,name="profile-update"),
    path(),
]
