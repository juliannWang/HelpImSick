import datetime
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from ImSick.models import UserAccount
from ImSick.models import Post
from ImSick.models import Comment
from django.shortcuts import redirect
from django.urls import reverse
from ImSick.forms import UserForm , PostForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.http import JsonResponse
import googlemaps
from django.contrib import messages


#working
@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('HelpImSick:login'))

#fixed, Working
@login_required
def index(request):
    account = UserAccount.objects.get(user=request.user)
    Posts = Post.objects.all()
    Comments = Comment.objects.all()
    context_dict = {}
    context_dict['posts'] = Posts
    context_dict['comments'] = Comments
    context_dict['accoount'] = account
    
    response = render(request, 'index.html' , context=context_dict)
    
    return response
    
#working  
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('HelpImSick:test'))
            else:
                return HttpResponse("Your HelpImSick account is disabled")
        
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')
#working
def createAccount(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            email = user.email
            userAccount = UserAccount.objects.get_or_create(user=user,email=email)[0]
            userAccount.save()

            registered = True

        else:
            messages.error(request, 'Username already exists')
            return render(request, 'register.html', context={'form': user_form,
                                                             'registered': registered})
        
        return redirect(reverse('HelpImSick:login'))

    else:
        user_form = UserForm()

    return render(request, 'register.html', context={'form': user_form,
                                                             'registered': registered})


#working
@login_required
def myPosts(request):

    userAccount = UserAccount.objects.get(user=request.user)
    posts = Post.objects.filter(postBy=userAccount)
    favPosts = userAccount.favoritePosts.all()

    context_dict = {'posts':posts}
    context_dict['user'] = userAccount
    context_dict['favPosts'] = favPosts

    response = render(request, 'myPosts.html', context=context_dict)
    return response

#working
@login_required
def createPost(request):
    if request.user.is_authenticated:
        username = request.user.username
        userAccount = UserAccount.objects.get(user=request.user)

        form = PostForm()

        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)

            if form.is_valid():
                post = form.save(commit=False)
                post.postLikes = 0
                post.postBy = userAccount
                post.postDate = timezone.now()
                if 'postImage' in request.FILES:
                    print("IMAGES IS HERE")
                    post.postImage = request.FILES['postImage']
                post.save()


                return redirect(reverse('HelpImSick:test'))
            else:
                print(form.errors)

        return render(request, 'createPost.html',context = {'form':form})

#working
@login_required   
def get_nearby_doctors(request):
    if request.method == 'GET':
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest': #checks if page is a ajax request
            api_key = 'AIzaSyBchxq-fKOpe1l1qeEZEX2NkseyzRbgnbs'
            client = googlemaps.Client(api_key)

            location = lat + "," +lon
            radius = 1500 # 1.5km

            place_type = 'doctor'

            result = client.places_nearby(location=location,radius=radius, type=place_type)

            places = result['results'][:3]

            nearby_docs = {}
            for i in range(3):
                placeid = places[i]['place_id']
                place_details = client.place(place_id = placeid)
                nearby_docs[i] = place_details

            return JsonResponse(nearby_docs, status=200)

    return render(request, 'nearby-Doctors.html')

#THIS WORKS LETS GOOOOOOOOO
@login_required
def postDetails(request,postID):
    postByID = Post.objects.get(postID=postID)
    comments = Comment.objects.filter(commentOnPost=postByID)
    userAccount = UserAccount.objects.get(user= request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        commentContent = request.POST.get('commentContent')
        if form.is_valid():
            comment = form.save(commit = False)
            comment.commentedBy = userAccount
            comment.commentOnPost = postByID
            comment.commentDate = timezone.now()
            comment.save()
            return redirect(reverse('HelpImSick:post', args = [postID]))
        else:
            print(form.errors)
    form = CommentForm()
    context_dict = {}
    context_dict["post"] = postByID
    context_dict["comments"] = comments
    context_dict["form"] = form
    context_dict["user"] = userAccount
    
    response = render(request,"postDetails.html",context = context_dict)
    return response

def deleteComment(request,postID,commentID):
    comment = Comment.objects.get(commentID = commentID)
    userAccount = UserAccount.objects.get(user=request.user)
    if (comment.commentedBy == userAccount):
        comment.delete()
     
    return redirect(reverse('HelpImSick:post', args = [postID]))


def deletePost(request,postID):
    postByID = Post.objects.get(postID=postID)
    comments = Comment.objects.filter(commentOnPost = postByID)
    for comment in comments:
        comment.delete()
    postByID.delete()
    return redirect(reverse('HelpImSick:myPosts'))

def likePost(request,postID):
    postByID = Post.objects.get(postID=postID)
    userAccount = UserAccount.objects.get(user=request.user)
    postByID.likedBy.add(userAccount)
    postByID.postLikes += 1
    postByID.save()
    return redirect(reverse('HelpImSick:post', args = [postID]))

def favouritePost(request,postID):
    postByID = Post.objects.get(postID=postID)
    userAccount = UserAccount.objects.get(user=request.user)
    if (postByID not in userAccount.favoritePosts.all()):
        userAccount.favoritePosts.add(postByID)
    userAccount.save()
    return redirect(reverse('HelpImSick:post', args = [postID]))

def unfavouritePost(request,postID):
    postByID = Post.objects.get(postID=postID)
    userAccount = UserAccount.objects.get(user=request.user)
    if (postByID in userAccount.favoritePosts.all()):
        userAccount.favoritePosts.remove(postByID)
    userAccount.save()
    return redirect(reverse('HelpImSick:post', args = [postID]))

def unlikePost(request,postID):
    postByID = Post.objects.get(postID=postID)
    userAccount = UserAccount.objects.get(user=request.user)
    postByID.likedBy.remove(userAccount)
    postByID.postLikes -= 1
    postByID.save()
    return redirect(reverse('HelpImSick:post', args = [postID]))


#working
@login_required
def add_comment(request,postID):
    post = Post.objects.get(postID = postID)
    userAccount = UserAccount.objects.get(user= request.user)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.commentedBy = userAccount
            comment.commentOnPost = post
            comment.save()
            return redirect(reverse('HelpImSick:post',
                                    kwargs={'postID':postID}))
        else:
            print(form.errors)
    context_dict = {'form':form}
    return HttpResponse("add_comment")

#working
@login_required
def searchPosts(request):
    query = request.GET.get('query')
    posts = Post.objects.filter(title__icontains=query) | Post.objects.filter(postContent__icontains=query)
    context_dict = {"query":query,"posts":posts}
    return render(request,"searchResults.html",context=context_dict)

@login_required
def settings(request):
    user = User.objects.get(id=request.user.id)
    userAccount = UserAccount.objects.get(user=request.user)
    
    
    if request.method == 'POST' :
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        name = request.POST.get('name', None)
        phoneNumber = request.POST.get('phone_number', None)
        about = request.POST.get('about', None)
        country = request.POST.get('country', None)
        language = request.POST.get('language', None)
        image_file = request.FILES.get('image', None)

        if username:
            user.username = username
        if password:
            user.set_password(password)
        if name:
            userAccount.name = name
        if phoneNumber:
            userAccount.phoneNumber = phoneNumber
        if about:
            userAccount.about = about
        if country:
            userAccount.country = country
        if language:
            userAccount.language = language
        if image_file:
            print("HELLO")
            userAccount.profilePicture = image_file
        user.save()
        userAccount.save()
    
    context_dict = {"user" : user , "userAccount":userAccount}


    response = render(request, 'settings.html', context=context_dict)

    return response

def viewProfile(request,username):
    user = User.objects.get(username=username)
    userAccount = UserAccount.objects.get(user=user)
    posts = Post.objects.filter(postBy=userAccount)
    favPosts = userAccount.favoritePosts.all()


    context_dict = {'posts':posts}
    context_dict['user'] = userAccount
    context_dict['favPosts'] = favPosts


    response = render(request, 'myPosts.html', context=context_dict)
    return response



