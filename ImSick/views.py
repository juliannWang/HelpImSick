from django.http import HttpResponse
from django.shortcuts import render
from ImSick.models import UserAccount
from ImSick.models import Post
from ImSick.models import Comment
from django.shortcuts import redirect
from django.urls import reverse
from ImSick.forms import UserForm ,UserProfileForm, PostForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.http import JsonResponse
import googlemaps


# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('HelpImSick:index'))
            else:
                return HttpResponse("Your HelpImSick account is disabled")
        
        else:
            print(f"Invalid login details: {email}, {password}")
            return HttpResponse("Email or password incorrect")

    else:
        return render(request, 'HelpImSick/login.html')

def createAccount(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'rango/register.html', context={'user_form': user_form,
                                                             'profile_form': profile_form,
                                                             'registered': registered})



@login_required
def myPosts(request):
    if request.user.is_authenticated:
        username = request.user.username

    post_list = Post.objects.order_by('postLikes')

    posts_by_user = []

    for post in post_list:
        if(post_list.postBy == username):
            posts_by_user.append(post)
    

    context_dict = {'posts':posts_by_user}

    response = render(request, 'HelpImSick/index/myPosts.html', context=context_dict)


@login_required
def createPost(request):
    if request.user.is_authenticated:
        username = request.user.username

        form = PostForm()

        if request.method == 'POST':
            form = PostForm(request.POST)

            if form.is_valid():
                post = form.save(commit=False)
                post.postLikes = 0
                post.postBy = username
                page.save()


                return redirect(reverse('HelpImSick: myPosts'))
            else:
                print(form.errors)


        context_dict = {'post':post}

        return render(request, 'HelpImSick/createPost.html')
    

class getNearbyDoctors(View):
    def get(self,request):
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

            nearbyDocs = {}
            for i in range(3):
                placeid = places[i]['place_id']
                place_details = client.place(place_id = placeid)
                nearbyDocs[i] = place_details

            return JsonResponse(nearbyDocs, status = 200)

        return render(request,'nearby-Doctors.html')





