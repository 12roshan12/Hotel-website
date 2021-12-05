from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db.models import fields
from .models import Blog, Enquiry, Events, User

class UserRegistrationForm(UserCreationForm):
    USER_CHOICE = (
        ('is_buyer', 'Is Employee'),
        ('is_seller', 'Is Customer'),
    )

    user_types = forms.CharField(label='User Type', widget=forms.RadioSelect(choices=USER_CHOICE))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('user',)
        fields = ['first_name', 'last_name', 'email']
        

class EnquiryForm(forms.ModelForm):
    
    class Meta:
        model = Enquiry
        fields = ['name','email','number','message']
        

class EventsForm(forms.ModelForm):

    class Meta:
        model = Events        
        fields = ['title','description','start_date','end_date','venue','added_by']

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        image = forms.ImageField()
        fields = ['title','description','image','added_by']        