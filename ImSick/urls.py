from django.urls import path
from ImSick import views

app_name = 'HelpImSick'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.createAccount, name='createAccount'),
    path('index/',views.index, name= "test"),
    #path('index/settings/', views.settings, name='settings'),
    path('post/<int:postID>', views.postDetails ,name='post'),
    path('post/<int:postID>/delete/', views.deletePost ,name='deletePost'),
    #path('index/search/', views.search, name='search'),
    #path('index/search/results', views.searchResults, name='searchResults'),
    path('index/createPost/', views.createPost, name='createPost'),
    path('index/my-posts/', views.myPosts, name='myPosts'),
    #path('index/nearestGP', views.nearestGp, name='nearestGP'),
    path('index/nearby-doctors/', views.get_nearby_doctors, name = 'nearby-doctors'),
    path('logout',views.user_logout,name="logout"),
    path('search/',views.searchPosts,name="search"),
    path('settings/',views.settings,name="settings")
]