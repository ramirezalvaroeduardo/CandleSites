from django.contrib import admin
from .models import CandleSite
from .models import Commentator
from .models import CandleSiteComments

class CandleAdmin(admin.ModelAdmin):
    list_display = ('id','companyName','companyLink','companyPhone', 'companyAddress')

class CommentatorAdmin(admin.ModelAdmin):
    list_display = ('id','userName','password')

class CandleCommentsAdmin(admin.ModelAdmin):
    list_display = ('id','candlesite','commentator','comment','rate')

admin.site.register(CandleSite, CandleAdmin)
admin.site.register(Commentator, CommentatorAdmin)
admin.site.register(CandleSiteComments, CandleCommentsAdmin)
