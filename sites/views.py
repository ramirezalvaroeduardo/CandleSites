from django.shortcuts import render
from .models import CandleSite

def sites(request):
	inventory = CandleSite.objects.all().count()
	context = {
		'inventory' : inventory,
	}
	print( 'Invetory: ',inventory )
	return render( request, 'sites.html', context )