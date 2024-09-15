from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required= False, help_text='Optional')
    last_name = forms.CharField(required= False, help_text='Optional')
    twitter_link = forms.CharField(required= False, help_text='Optional. Start With "http://" or "https://"')
    facebook_link = forms.CharField(required= False, help_text='Optional. Start With "http://" or "https://"')
    instagram_link = forms.CharField(required= False, help_text='Optional. Start With "http://" or "https://"')
    linkedin_link = forms.CharField(required= False, help_text='Optional. Start With "http://" or "https://"')
    profile_picture = forms.ImageField(required=True)
    usable_password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_picture', 'bio', 'twitter_link', 'facebook_link', 'instagram_link', 'linkedin_link', 'password1', 'password2']
