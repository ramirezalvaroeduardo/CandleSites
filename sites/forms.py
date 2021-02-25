from django import forms
from .models import CandleSite
from .models import CandleSiteComments
from .models import Commentator

from django.contrib.auth.models import User


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
            'companyAddress',
        ]

class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea, label='Comment')
    comment.widget.attrs.update({'class': 'commTextClass'})
    rate = forms.IntegerField(label='Rate')
    rate.widget.attrs.update({'class': 'dInput'})
    class Meta:
        model = CandleSiteComments
        exclude = (
            'candlesite',
            'commentator',
        )
        fields = [
            'comment',
            'rate',
        ]

class registerForm(forms.ModelForm):
    username = forms.CharField(label='User Name')
    username.widget.attrs.update({'class': 'dInput'})
    password = forms.CharField(max_length=16, widget=forms.PasswordInput,label='Password')
    password.widget.attrs.update({'class': 'dInput'})
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
