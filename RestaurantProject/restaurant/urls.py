from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("menu/", views.menu, name="menu"),
    path("about/", views.about, name="about"),
    path("menu/add/", views.add_dish, name="add_dish"),
    path("menu/edit/<int:pk>/",views.EditDish.as_view(),name="edit_dish"),
    path("menu/delete/<int:pk>/",views.delete_dish,name="delete_dish"),
    ]