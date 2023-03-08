from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from ImSick.form import RegistrationForm
from .models import UserAccount


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            name = request.POST.get('name')
            phoneNumber = request.POST.get('phoneNumber')
            email = request.POST.get('email')
            about = request.POST.get('about')
            country = request.POST.get('country')
            language = request.POST.get('language')
            profilePicture = request.FILES.get('profilePicture')
            UserAccount.objects.create(
                user=user,
                name=name,
                phoneNumber=phoneNumber,
                email=email,
                about=about,
                country=country,
                language=language,
                profilePicture=profilePicture,
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def search_posts(request):
    return render(request, 'search_posts.html', )
