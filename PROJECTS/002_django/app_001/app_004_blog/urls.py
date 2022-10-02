from django.urls import path
from . import views

app_name="app4"

urlpatterns = [
    path("dashboard/",views.dashboard ,name="name_dashboard"),
    path("articles/",views.articles ,name="name_articles"),
    path("detail/<int:id>",views.detail ,name="name_detail"),
    path("addarticle/",views.article_add ,name="name_addarticle"),
    path("deletearticle/<int:id>",views.article_delete ,name="name_deletearticle"),
    path("uptadearticle/<int:id>",views.article_update ,name="name_updatearticle"),
    
]