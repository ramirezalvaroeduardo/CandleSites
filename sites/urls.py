from django.urls import path
from . import views

urlpatterns = [
    path('', views.siteLinks, name='siteLinks'),
    path('sites/', views.sites, name='sites'),
    path('register/', views.register, name='Register'),
    path('about/', views.about, name='about'),
    path('siteLinks/', views.siteLinks, name='siteLinks'),
    path('template/', views.template, name='template'),
]