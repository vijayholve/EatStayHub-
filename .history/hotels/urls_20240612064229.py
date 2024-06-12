
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("base.urls")),
    path("rooms/",include("rooms.urls")),
    path("profile/<str:pk>/",include("accounts.urls")),
    path("restaurant-data/",include("restaurant.urls")),
    path("api/",include("api.urls")),
]   
