from os import name
from django.urls import path
from . import views

urlpatterns = [
  path("logout", views.logout_view, name= "logout")
    ,path("addreadlater",views.addreadlater.as_view(),name="addme")
    ,path("register",views.Register.as_view(),name="register")
    ,path("login",views.Login.as_view(),name="login"),
    path("", views.home_page , name="home"),
    path("post", views.post_page.as_view() , name="all_post"),
    path("<slug:post_slag>", views.post.as_view() , name="post")
    
]