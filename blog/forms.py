from django import forms

from .models import *

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['category', 'title', 'content', 'image', 'status']
        widgets = {
            'category': forms.CheckboxSelectMultiple(),
            }
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required= False, help_text='Optional')
    last_name = forms.CharField(required= False, help_text='Optional')
    twitter_link = forms.CharField(required= False, help_text='Optional. Start With "http://" or "https://"')
    facebook_link = forms.CharField(required= False, help_text='Optional. Start With "http://" or "https://"')
    instagram_link = forms.CharField(required= False, help_text='Optional. Start With "http://" or "https://"')
    linkedin_link = forms.CharField(required= False, help_text='Optional. Start With "http://" or "https://"')
    profile_picture = forms.ImageField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_picture', 'bio', 'twitter_link', 'facebook_link', 'instagram_link', 'linkedin_link']
