
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class VendorRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    business_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class VendorLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
