from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts.views import create_profile

urlpatterns = [
path("",views.home,name="home"),
path("login-page/",views.login_page,name="login-page"),
path("logout-page/",views.logout_page,name="logout-page"),    
path("register/",views.register,name="register"),
path("restaurant-create/",views.create_restaurant,name="restaurant-create"),
path("restaurant-data/<str:pk>/",views.restaurant_data,name="restaurant-data"),
path("restaurant-update/<str:pk>/",views.update_restaurant,name="restaurant-update"),
path("restaurant-delete/<str:pk>/",views.delete_restaurant,name="restaurant-delete"),
path("dish-create/<str:pk>/",views.create_dish,name="dish-create"), 

path("dish-delete/<str:pk>/",views.delete_dish,name="dish-delete"),
path("dish-update/<str:pk>/",views.update_dish,name="dish-update"), 
# path("celery/",views.views_fun,name="test"), 
    path("create-profile/",create_profile,name="create-profile"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,
                        document_root =settings.MEDIA_ROOT)
    
