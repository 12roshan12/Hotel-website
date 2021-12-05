from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from .models import Staff
from django import forms

class StaffRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    class Meta:
        model = Staff 
        fields = ['first_name','last_name','email','phone_number','password']

