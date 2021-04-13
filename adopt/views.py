

from django.shortcuts import render
from .models import Sighting
from django.shortcuts import redirect
from .forms import SquirrelMap


# Create your views here.
def homepage_view(request):
    return render(request,'Sightings/homepage.html')

def map_view(request):
    sights = Sighting.objects.all()[:100]
    context = {
            'sights':sights,
            }
    return render(request, 'Sightings/map.html', context)


def list_sights(request):
    sights = Sighting.objects.all()
    fields = ['Unique_Squirrel_Id','Longtitude','Latitude','Date','Shift']
    context = {
            'sights':sights,
            'fields':fields,
            }
    return render(request, 'Sightings/list.html', context)


def update_sights(request,Unique_Squirrel_Id):
    sight = Sighting.objects.get(Unique_Squirrel_Id=Unique_Squirrel_Id)
    if request.method == 'POST':
        form = SquirrelMap(request.POST, instance = sight)
        if form.is_valid():
            form.save()
            return redirect(f'/Sightings')
        else:
            return JsonResponse({'errors':form.errors}, status=400)
    else:
        form = SquirrelMap(instance = sight)

    context = {
            'form':form,
            }
    return render(request, 'Sightings/update.html', context)


def add_sights(request):
    if request.method == 'POST':
        form = SquirrelMap(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/Sightings/')
    else:
        form = SquirrelMap()

    context = {
            'form':form,
            }

    return render(request, 'Sightings/add.html', context)

def stats(request):
	squirrels = Sighting.objects.all()
	total = len(squirrels)
	lattitude = squirrels.aggregate(minimum=Min('Latitude'),maximum=Max('Latitude'))
	longitude = squirrels.aggregate(minimum=Min('Longitude'),maximum=Max('Longitude'))
	primary_fur_color =list(squirrels.values_list('Primary_Fur_Color').annotate(Count('Primary_Fur_Color')))
	running = list(squirrels.values_list('Running').annotate(Count('Running')))
	shift = list(squirrels.values_list('Shift').annotate(Count('Shift')))
	context = {'total': total,
		'lattitude': lattitude,
		'longitude': longitude,
		'primary_fur_color': primary_fur_color,
		'running': running,
		'shift': shift,
		}
	return render(request, 'sightings/stats.html', context)
