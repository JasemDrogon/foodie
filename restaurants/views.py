from django.shortcuts import render
from django.shortcuts import render
import random
from .models import Restaurant

# Create your views here.

def restaurant_list(request):
	rest_objects = Restaurant.objects.all()

	return render(request, 'restaurant_list.html', context)

def restaurant_detail(request, restaurant_id):
	thing = Restaurant.objects.get(id=restaurant_id)

	return render(request, 'restaurant_detail.html', context)