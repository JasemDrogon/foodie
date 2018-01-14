from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantForm

# Create your views here.

def restaurant_list(request):
	rest_objects = Restaurant.objects.all()
	context = {
	"restauarants": rest_objects
	}

	return render(request, 'restaurants_list.html', context)

def restaurant_detail(request, restaurant_id):
	thing = Restaurant.objects.get(id=restaurant_id)
	context = {
		"festaurant": thing
	}
	return render(request, 'restaurants_detail.html', context)



def restaurant_create(request):
	form =RestaurantForm(request.POST or None)
	if form.is_valid():

		form.save()

		return redirect("restaurant_list")
	context = {

	"restaurant" : form 
	}

	return render(request, "restaurant_create.html", context)

def restaurant_update(request,restaurant_id):

	item = Restaurant.objects.get(id= restaurant_id)
	form = RestaurantForm(instance = item)

	if request.method == "POST":

		form = RestaurantForm(request.POST or None, instance = item)

	
	if form.is_valid():
		form.save()
		return redirect("restaurant_detail", restaurant_id=restaurant_id)

	context = {

	"form": form,
	"item": item,	

	}

	return render(request, "restaurant_update.html", context)

def restaurant_delete(request,restaurant_id):
	Restaurant.objects.get(id=restaurant_id).delete()

	return redirect("restaurant_list")