from django.shortcuts import render
from .models import CandleSite

def sites(request):
	inventory = CandleSite.objects.all().count()
	context = {
		'inventory' : inventory,
		'appName' : 'welcome to candle stores',
	}
	print( 'Invetory: ',inventory )
	return render( request, 'sites.html', context )

def template(request):
	return render( request, 'template.html')