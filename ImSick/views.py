import datetime
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
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


# Create your views here.
@login_required
def test(request):
    print("*********************** request ************************")
    print(request.user.id)
    return HttpResponse("test")

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
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Email or password incorrect")

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
            print(user_form.errors)
        
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

    context_dict = {'posts':posts}

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
    
    response = render(request,"postDetails.html",context = context_dict)
    return response

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



