
from django.urls import path
from . import views

app_name="app2"

urlpatterns = [
    path('about/', views.about,name="name_about"),
    path('personals/', views.personal,name="name_personal"),
    path('delete/<int:id>/', views.delete_function,name="name_delete"),
    path('update/<int:id>/', views.update_function,name="name_update"),
]




"""

name : iko
password : 1

"""