from django import forms
from ImSick.models import UserAccount, Post, Comment
from django.contrib.auth.models import User
from datetime import datetime

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phoneNumber','about','country','language','profilePicture',)


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100, help_text="Give your post a title")
    postContent = forms.CharField(max_length=1000, help_text="Post text goes here")
    postImage = forms.ImageField()
    postDate = datetime.now()

    class meta:
        model = Post
        exclude = ('postBy')
