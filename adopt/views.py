

from django.shortcuts import render
from django.db import models
from .models import Sighting
from django.shortcuts import redirect
from .forms import SquirrelMap
from django.db.models import Avg, Max, Min, Count
from django.shortcuts import get_object_or_404


# Create your views here.

def map_view(request):
	squirrels = Sighting.objects.all()[:100]
	context = {'squirrels': squirrels}
	return render(request, 'adopt/map.html', context)

def homepage_view(request):
    return render(request,'adopt/homepage.html')

def list_sights(request):
    sights = Sighting.objects.all()
    fields = ['Unique_Squirrel_ID','Longtitude','Latitude','Date','Shift']
    context = {
            'sights':sights,
            'fields':fields,
            }
    return render(request, 'adopt/list.html', context)


def update_sights(request,**Unique_Squirrel_Id):
    sight = Sighting.objects.get(Unique_Squirrel_ID=Unique_Squirrel_Id)
    if request.method == 'POST':
        form = SquirrelMap(request.POST, instance = sight)
        if form.is_valid():
            form.save()
            return redirect(f'/adopt')
    else:
        form = SquirrelMap(instance = sight)

    context = {
            'form':form,
            }
    return render(request, 'adopt/update.html', context)

def add_sights(request):
    if request.method == 'POST':
        form = SquirrelMap(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/adopt/')
    else:
        form = SquirrelMap()

    context = {
            'form':form,
            }

    return render(request, 'adopt/add.html', context)

def stats(request):
	squirrels = Sighting.objects.all()
	total = len(squirrels)
	lattitude = squirrels.aggregate(maximum=Max('Latitude'))
	longitude = squirrels.aggregate(maximum=Max('Longitude'))
	age =list(squirrels.values_list('Age').annotate(Count('Age')))
	running = list(squirrels.values_list('Running').annotate(Count('Running')))
	location = list(squirrels.values_list('Location').annotate(Count('Location')))
	context = {'total': total,
		'lattitude': lattitude,
		'longitude': longitude,
		'age': age,
		'running': running,
		'location': location,
		}
	return render(request, 'adopt/stats.html', context)
