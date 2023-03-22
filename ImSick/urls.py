from django.urls import path
from ImSick import views

app_name = 'HelpImSick'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.createAccount, name='createAccount'),
    path('index/',views.index, name= "test"),
    path('post/<int:postID>', views.postDetails ,name='post'),
    path('post/<int:postID>/delete/', views.deletePost ,name='deletePost'),
    path('post/<int:postID>/like/', views.likePost ,name='likePost'),
    path('post/<int:postID>/unlike/', views.unlikePost ,name='unlikePost'),
    path('post/<int:postID>/deletecomment/<int:commentID>/',views.deleteComment,name="deleteComment"),
    path('index/createPost/', views.createPost, name='createPost'),
    path('my-posts/', views.myPosts, name='myPosts'),
    path('nearby-doctors/', views.get_nearby_doctors, name = 'nearby-doctors'),
    path('logout',views.user_logout,name="logout"),
    path('search/',views.searchPosts,name="search"),
    path('settings/',views.settings,name="settings"),
    path('viewprofile/<str:username>/',views.viewProfile,name="viewProfile")
]