from django.db import models
from django.utils import timezone

class CandleSite(models.Model):
    companyName = models.CharField(max_length=120)
    companyLink = models.CharField(max_length=200)
    companyPhone = models.CharField(max_length=20)
    companyAddress = models.CharField(max_length=150)
    
