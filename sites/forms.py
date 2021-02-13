from django import forms
from .models import CandleSite

class CandleSiteForm(forms.ModelForm):
    class Meta:
        model = CandleSite
        fields = [
            'companyName',
            'companyLink',
            'companyPhone',
            'companyAddress',
        ]

