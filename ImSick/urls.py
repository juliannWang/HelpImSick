from django.urls import path
from ImSick import views

app_name = 'HelpImSick'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('createAccount/', views.createAccount, name='createAccount'),
    #path('index/settings/', views.settings, name='settings'),
    path('post/<int:postID>', views.postDetails ,name='post'),
    #path('index/search/', views.search, name='search'),
    #path('index/search/results', views.searchResults, name='searchResults'),
    path('createPost/', views.createPost, name='createPost'),
    path('index/myPosts/', views.myPosts, name='myPosts'),
    #path('index/nearestGP', views.nearestGp, name='nearestGP'),
    path('nearby-doctors/', views.get_nearby_doctors, name = 'nearby-doctors'),
    path('test',views.index, name= "test"),
    path('logout',views.user_logout,name="logout"),
    path('search/',views.searchPosts,name="search"),
]