from django.shortcuts import render
from .forms import CandleSiteForm
from .forms import CommentForm
from .forms import registerForm
from .models import CandleSite
from .models import CandleSiteComments
from .models import Commentator
from django.core import serializers

def sites(request):
	inventory = CandleSite.objects.all().count()
	context = {
		'inventory' : inventory,
		'appName' 	: 'welcome to candle stores',
	}
	print( 'Inventory: ',inventory )
	return render( request, 'sites.html', context )

def register(request):
	userForm = registerForm(request.POST or None)
	if userForm.is_valid():
		userForm.save()
	context = {
		'pageTitle' : 'Register',
		'form'      : userForm,
	}
	return render(request, 'register.html', context)

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
	sitesJson	= serializers.serialize('json', siteLinks)
	commJson	= serializers.serialize('json', siteComments)
	commtrsJson	= serializers.serialize('json', commentators)
	
	form = CandleSiteForm(request.POST or None)
	commForm = CommentForm(request.POST or None)
	if form.is_valid():
		form.save()
	if commForm.is_valid():
    		commForm.save()
	context = {
		'pageTitle' : pageTitle,
		'recnum'    : recNum,
		'sitelinks'	: siteLinks,
		'siteInfo'  : sitesJson,
		'siteComms'	: commJson,
		'commtrs'	: commtrsJson,
		'form'      : form,
		'commForm'  : commForm,
	}
	return render(request, 'siteLinks/siteLinks.html', context)

def createSiteLinks(request):
    form = CandleSiteForm(request.POST or None)
