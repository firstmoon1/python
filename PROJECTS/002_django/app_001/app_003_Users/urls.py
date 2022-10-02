from django.urls import path
from . import views

app_name ="app3"

urlpatterns = [
    path("register/",views.register_func , name="name_register"),
    path("login/",views.login_func , name="name_login"),
    path("logout/",views.logout_func , name="name_logout"),
]




