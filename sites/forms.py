from django import forms
from .models import CandleSite

class CandleSiteForm(forms.ModelForm):

    companyName = forms.CharField(label='Company Name')
    companyLink = forms.CharField(label='Company Site')
    companyPhone = forms.CharField(label='Company Phone')
    companyAddress = forms.CharField(label='Company Address')

    companyName.widget.attrs.update({'class': 'dInput'})
    companyLink.widget.attrs.update({'class': 'dInput'})
    companyPhone.widget.attrs.update({'class': 'dInput'})
    companyAddress.widget.attrs.update({'class': 'dInput'})

    class Meta:
        model = CandleSite
        fields = [
            'companyName',
            'companyLink',
            'companyPhone',
            'companyAddress'
        ]
