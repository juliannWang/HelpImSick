from django import forms
from ImSick.models import UserAccount, Post, Comment
from django.contrib.auth.models import User
from rango.models import UserProfile
from datetime import datetime

class UserForm(forms.modelForm):
    name = forms.CharField(max_lenth=50, help_text="Please enter a username")
    password = forms.CharField(widget=forms.PasswordInput)
    phoneNumber = forms.IntegerField(max_length=20, help_text="Please enter your phone number")
    email = forms.EmailField(max_length=50, help_text="Please enter your e-mail address")
    about = forms.CharField(max_length=200, help_text="This is the about section, write some things about yourself")
    country = forms.CharField(max_length=30, help_text="Please enter the country you are from")
    language = forms.CharField(max_length=30, help_text="Please enter your preferred language")
    profile_picture = forms.ImageField(widget=forms.ImageField)

    class meta:
        model = UserAccount
        fields = ('name',)


class PostForm(forms.modelForm):
    title = forms.CharField(max_length=100, help_text="Give your post a title")
    postContent = forms.CharField(max_length=1000, help_text="Post text goes here")
    postImage = forms.ImageField(widget=forms.ImageField)
    postDate = datetime.now()
