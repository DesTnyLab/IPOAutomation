from django import forms
from .models import AccountDetials


class AccountDetailsForm(forms.ModelForm):

    class Meta:
        model = AccountDetials
        fields = ['name','dp_id', 'username', 'password', 'crn_number', 'pin']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'dp_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DP ID'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'crn_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CRN Number'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'pin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PIN'}),
        }


