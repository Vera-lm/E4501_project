

from django.shortcuts import render
from .models import Sighting
from django.shortcuts import redirect
from .forms import SquirrelMap


# Create your views here.

def map(request):
	squirrels = Sighting.objects.all()[:100]
	context = {'squirrels': squirrels}
	return render(request, 'adopt/index.html', context)

def homepage(request):
    return render(request,'adopt/homepage.html')

def list_sights(request):
    sights = Sighting.objects.all()
    fields = ['Unique_Squirrel_ID','Longtitude','Latitude','Date','Shift']
    context = {
            'sights':sights,
            'fields':fields,
            }
    return render(request, 'adopt/list.html', context)


def update_sights(request,Unique_Squirrel_ID):
    sight = Sighting.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method == 'POST':
        form = SquirrelMap(request.POST, instance = sight)
        if form.is_valid():
            form.save()
            return redirect(f'/adopt')
        else:
            return JsonResponse({'errors':form.errors}, status=400)
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
	return render(request, 'adopt/stats.html', context)
