"""HelpImSick URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from ImSick import views

app_name = 'HelpImSick'

urlpatterns = [
    path('index/',views.index, name='index'),  
    path('login/', views.login, name='index'), 
    path('logout/', views.user_logout, name='logout'),  
    path('createAccount/', views.createAccount, name='createAccount'), 
    path('index/settings/', views.settings, name='settings'), 
    path('index/post/<slug:post_id_slug>', views.post, name='post'),
    path('index/search/', views.search, name='search'),
    path('index/search/results', views.searchResults, name='searchResults'),
    path('index/createPost/', views.createPost, name='createPost'),   
    path('index/myPosts/', views.myPosts, name='myPosts'),   
    path('index/nearestGP', views.nearestGp, name='nearestGP'),
    path('accounts/', include('registration.backends.simple.urls')),
    
]