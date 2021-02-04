from django.urls import path
from . import views

urlpatterns = [
    path('', views.sites, name='sites'),
    path('template/', views.template, name='template'),
]