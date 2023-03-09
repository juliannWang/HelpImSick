from django.db import models
from django.contrib.auth.models import User


class UserAccount(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    # additional attributes
    name = models.CharField(max_length=50)
    phoneNumber = models.IntegerField()
    email = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
    country = models.CharField(max_length=30)
    language = models.CharField(max_length=30)
    profilePicture = models.ImageField(
        upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    postID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    postContent = models.CharField(max_length=1000)
    postImage = models.ImageField(upload_to='images', blank=True)
    postDate = models.DateTimeField()
    postLikes = models.IntegerField(default=0)
    postBy = models.ForeignKey(
        UserAccount, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    commentID = models.AutoField(primary_key=True)
    commentedBy = models.ForeignKey(
        UserAccount, on_delete=models.SET_NULL, null=True)
    commentOnPost = models.ForeignKey(
        Post, on_delete=models.SET_NULL, null=True)
    commentDate = models.DateTimeField()
    commentContent = models.CharField(max_length=50)
