from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('search_posts/', views.search_posts, name='search-posts'),
]
