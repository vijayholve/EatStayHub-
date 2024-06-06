from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.profile,name="profile"),
    path("profile-updat/e",views.update_profile,name="profile-update"),
    path("create-profile/",views.create_profile,name="create-profile"),
]
