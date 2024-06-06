from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.,name="profile"),
    path("profile-update/",views.update_profile,name="profile-update"),
    path("create-profile/",views.create_profile,name="create-profile"),
]
