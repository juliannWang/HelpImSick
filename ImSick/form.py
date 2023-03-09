from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserAccount


class RegistrationForm (UserCreationForm):
    name = forms.CharField(max_length=255)
    phoneNumber = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=255)
    about = forms.CharField(widget=forms.Textarea)
    country = forms.CharField(max_length=255)
    language = forms.CharField(max_length=255)
    profilePicture = forms.ImageField(required=False)

    class Meta:
        model = UserAccount
        fields = ['password1', 'password2', 'name', 'phoneNumber',
                  'email', 'about', 'country', 'language', 'profilePicture']
