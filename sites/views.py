from django.shortcuts import render, redirect
from .forms import CandleSiteForm
from .forms import CommentForm
from .forms import registerForm
from .models import CandleSite
from .models import CandleSiteComments
from .models import Commentator
from django.core import serializers

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm




def sites(request):
	inventory = CandleSite.objects.all().count()
	context = {
		'inventory' : inventory,
		'appName' 	: 'welcome to candle stores',
	}
	print( 'Inventory: ',inventory )
	return render( request, 'sites.html', context )

def register(request):
	userForm = UserCreationForm(request.POST or None)
	if userForm.is_valid():
		userForm.save()
		return redirect('/sites/siteLinks')
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

def siteLinks(request):
	#if request.user.is_authenticated:
		#return redirect(settings.LOGIN_URL)
	candlesite = 0;
	pageTitle	= 'Store Sites - ' + str( request.user.id )
	recNum		= CandleSite.objects.all().count()
	siteLinks	= CandleSite.objects.all().order_by('companyName')
	siteComments= CandleSiteComments.objects.all()
	commentators= Commentator.objects.all()
	currUsers	= User.objects.all()
	sitesJson	= serializers.serialize('json', siteLinks)
	commJson	= serializers.serialize('json', siteComments)
	commtrsJson	= serializers.serialize('json', commentators)
	candleForm = CandleSiteForm(request.POST or None)
	commForm = CommentForm(request.POST or None)
	if candleForm.is_valid() and commForm.is_valid():
		if not request.user.is_authenticated:
			return redirect(settings.LOGIN_URL)
		candlesite = candleForm.save()
		comment    = commForm.save(commit=False)
		comment.candlesite = candlesite
		comment.commentator = User.objects.get(id=request.user.id)
		comment.save()

	context = {
		'pageTitle' : pageTitle,
		'recnum'    : recNum,
		'sitelinks'	: siteLinks,
		'siteInfo'  : sitesJson,
		'siteComms'	: commJson,
		'commtrs'	: commtrsJson,
		'candleForm': candleForm,
		'commForm'  : commForm,
	}
	return render(request, 'siteLinks/siteLinks.html', context)
