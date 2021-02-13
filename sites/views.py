from django.shortcuts import render
from .forms import CandleSiteForm
from .models import CandleSite

def home(request):
	context = {
		'pageTitle' : 'CandleSites Home Page'
	}
	return render(request, 'home.html', context )

def sites(request):
	inventory = CandleSite.objects.all().count()
	context = {
		'inventory' : inventory,
		'appName' : 'welcome to candle stores',
	}
	print( 'Inventory: ',inventory )
	return render( request, 'sites.html', context )

def contact(request):
	context = {
		'pageTitle' : 'Contact'
	}
	return render(request, 'contact.html', context)

def about(request):
	context = {
		'pageTitle' : 'About',
		'content' : 'This is the About content',
	}
	return render(request, 'about.html', context)

def siteLinks(request):
	inventory = CandleSite.objects.all().count()
	item = CandleSite.objects.get(id=35)
	context = {
		'inventory' : inventory,
		'headLine' : 'List of Candle Site Links',
		'item' : item,
	}
	return render( request, 'siteLinks.html', context)


def template(request):
	return render( request, 'template.html')

def siteLinks(request):
	pageTitle = 'Store Links'
	inventory = CandleSite.objects.all().count()
	item      = CandleSite.objects.get(id=24)
	siteLinks = CandleSite.objects.all();
	form = CandleSiteForm(request.POST or None)
	if form.is_valid():
		form.save()
	context = {
		'pageTitle' : pageTitle,
		'inventory' : inventory,
		'item'      : item,
		'sitelinks' : siteLinks,
		'form'      : form,
	}
	return render(request, 'siteLinks/siteLinks.html', context)

def createSiteLinks(request):
    form = CandleSiteForm(request.POST or None)
