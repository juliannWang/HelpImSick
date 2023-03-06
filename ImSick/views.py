from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required
def user_logout(request):
    logout(request)

    return redirect(reverse('HelpImSick:index'))