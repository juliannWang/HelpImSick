from django.urls import path
from rango import views

app_name = 'HelpImSick'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='index'),
    path('createAccount/', views.createAccount, name='createAccount'),
    path('index/settings/', views.settings, name='settings'),
    path('index/post/<slug:post_id_slug>', views.post name='post'),
    path('index/search/', views.search, name='search'),
    path('index/search/results', views.searchResults, name='searchResults'),
    path('index/createPost/', views.createPost, name='createPost'),
    path('index/myPosts/', views.myPosts, name='myPosts'),
    path('index/nearestGP', views.nearestGp, name='nearestGP'),
]