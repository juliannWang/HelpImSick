from django import forms
from ImSick.models import UserAccount, Post, Comment
from django.contrib.auth.models import User
from datetime import datetime
from django.db import models

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ('phoneNumber','about','country','language','profilePicture',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','postContent','postImage')
        exclude = ('postBy','')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('commentContent',)
        widgets = {
            'commentContent':forms.Textarea(attrs={'rows':4, 'cols':40}),
        }
        