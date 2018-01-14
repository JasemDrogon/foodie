from django.contrib import admin
from django.urls import path, include

from restaurants import views

urlpatterns = [
    path('restaurant_list/', views.restaurant_list, name='restaurant_list'),
    path('restaurant_detail/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('restaurant_update/<int:restaurant_id>/',views.restaurant_update, name="restaurant_update"),
    path('restaurant_delete/<int:restaurant_id>/',views.restaurant_delete, name="restaurant_delete"),
    path('restaurant_create/',views.restaurant_create, name="restaurant_create"),

    ]
