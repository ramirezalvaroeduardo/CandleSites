from django.contrib import admin
from .models import CandleSite

class CandleAdmin(admin.ModelAdmin):
    list_display = ('companyName','companyLink','companyPhone', 'companyAddress')

admin.site.register(CandleSite, CandleAdmin)
