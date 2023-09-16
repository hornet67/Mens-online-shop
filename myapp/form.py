from django.forms import  ModelForm
from django import forms

from .models import Signup


class RegistrationForm(ModelForm):

    class Meta:
        model = Signup
        fields = ['name', 'email','password']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Your Password'}),
        }

