from django.shortcuts import render
from ImSick.models import UserAccount
from ImSick.models import Post
from ImSick.models import Comment
from ImSick.forms import UserForm
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required
def user_logout(request):
    logout(request)

    return redirect(reverse('HelpImSick:homepage'))


def index(request):
    post_list=Post.objects
    comments=Comment.objects

    context_dict = {}
    context_dict['posts']=post_list
    context_dict['account']=UserAccount
    context_dict['comments']=comments

     
    response = render(request, 'rango/index.html', context=context_dict)
    
    return response