from django.shortcuts import render
from .forms import CandleSiteForm
from .models import CandleSite
from .models import CandleSiteComments
from .models import Commentator
from django.core import serializers

def home(request):
	context = {
		'pageTitle' : 'CandleSites Home Page'
	}
	return render(request, 'home.html', context )

def sites(request):
	inventory = CandleSite.objects.all().count()
	context = {
		'inventory' : inventory,
		'appName' 	: 'welcome to candle stores',
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
		'content' 	: 'This is the About content',
	}
	return render(request, 'about.html', context)

def template(request):
	return render( request, 'template.html')

def siteLinks(request):
	pageTitle	= 'Store Sites'
	recNum		= CandleSite.objects.all().count()
	siteLinks	= CandleSite.objects.all().order_by('companyName')
	siteComments= CandleSiteComments.objects.all()
	commentators= Commentator.objects.all()
	commJson	= serializers.serialize('json', siteComments)
	commtrsJson	= serializers.serialize('json', commentators)
	
	form = CandleSiteForm(request.POST or None)
	if form.is_valid():
		form.save()
	context = {
		'pageTitle' : pageTitle,
		'recnum'    : recNum,
		'sitelinks' : siteLinks,
		'siteComms'	: commJson,
		'commtrs'	: commtrsJson,
		'form'      : form,
	}
	return render(request, 'siteLinks/siteLinks.html', context)

def createSiteLinks(request):
    form = CandleSiteForm(request.POST or None)
