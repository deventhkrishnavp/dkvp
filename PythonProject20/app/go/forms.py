from django import forms
from .models import Package

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['img', 'name', 'price', 'destination', 'desc', 'is_top', 'expiry_date']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }

        labels = {
            'img':"IMAGE",
            'name':"NAME",
            'price':"PRICE",
            'destination':"DESTINATIONS",
            'des':"DESCRIPTIONS",
            'is_top':"TOP PACKAGE?"
        }

from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'cus_name': forms.TextInput(attrs={'class': 'form-control'}),
            'cus_phn': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'cus_name': 'Customer Name',
            'cus_phn': 'Phone Number',
            'package': 'Select Package',
            'booking_date': 'Travel Date',
            'booked_on': 'Booked On',
        }
