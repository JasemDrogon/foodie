from django.contrib import admin
from django.urls import path, include

from restaurants import views

urlpatterns = [
    path('restaurant_list/', views.restaurants_list.url, name='restaurant_list'),
    path('restaurant_detail/<int:restaurant_id>/', views.restaurants_detail.url, name+'restaurant_detail')
]

