from django.shortcuts import render
from ImSick.models import UserAccount
from ImSick.models import Post
from ImSick.models import Comment
from ImSick.forms import UserForm
from ImSick.forms import UserProfileForm
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

     
    response = render(request, 'ImSick/index.html', context=context_dict)
    
    return response


@login_required
def settings(request):
    if request.method == 'POST' :
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        user_form = UserForm(data=request.POST)

        if profile_form.is_valid():
            profile_form.save()
            return redirect('settings')

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)

            user.save
        else:
            user_form = UserForm()
    else:
        profile_form = UserProfileForm(instance=request.user.profile)
        user_form = UserForm(instance=request.user)

    response = render(request, 'ImSick/index/settings.html', {'profile_form' : profile_form, 'user_form' : user_form})

    return response

@login_required
def delete_comment(request, commentID):

    if request.method == 'POST':
        comment = Comment.objects.get(commentID=commentID)
        postID = comment.commentOnPost.postID

        if comment.commentedBy.user == request.user:
            comment.delete()

    return redirect(reverse('HelpImSick:post', args=[postID]))