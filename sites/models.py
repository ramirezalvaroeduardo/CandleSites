from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class CandleSite(models.Model):
    companyName     = models.CharField(max_length=128)
    companyLink     = models.CharField(max_length=256)
    companyPhone    = models.CharField(max_length=24)
    companyAddress  = models.CharField(max_length=128)
    
class Commentator(models.Model):
    userName        = models.CharField(max_length=128)
    password        = models.CharField(max_length=16)

class CandleSiteComments(models.Model):
    candlesite      = models.ForeignKey(CandleSite, on_delete=models.CASCADE)
    commentator     = models.ForeignKey(Commentator, on_delete=models.CASCADE)
    comment         = models.CharField(max_length=1024)
    rate            = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

