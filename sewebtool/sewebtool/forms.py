from django import forms
from .models import TransitAgency
from .models import Vehicle

class TransitData(forms.ModelForm):
    class Meta:
        model = TransitAgency
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter the long name for the Transit Agency',
                'class': 'form-control'
            }),
            'abbreviation': forms.TextInput(attrs={
                'placeholder': 'Enter the abbreviation',
                'class': 'form-control'
            }),
            'city': forms.TextInput(attrs={
                'placeholder': 'Enter the City',
                'class': 'form-control'
            }),
            'state': forms.TextInput(attrs={
                'placeholder': 'Enter the state abbreviation',
                'class': 'form-control'
            }),
            'customer_account_number': forms.NumberInput(attrs={
                'placeholder': 'Enter the customer account number',
                'class': 'form-control'
            }),
        }
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_type', 'customer', 'build_manufacturer', 'build_year']
        widgets = {
            'vehicle_type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter vehicle type (e.g., Sedan, SUV, etc.)'
            }),
            'customer': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter customer name'
            }),
            'build_manufacturer': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter manufacturer name'
            }),
            'build_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter build year'
            }),
        }
