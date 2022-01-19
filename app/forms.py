from django import forms
from django.forms import ModelForm
from .models import *

class CustomerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        
    # create meta class
    class Meta:
        # specify model to be used
        model = Customers
        fields = '__all__' 
        labels = {'dob': 'Date of birth (yyyy-mm-dd)', 'since': 'Since (yyyy-mm-dd)'}