from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    
    #additional attributes
    name = models.CharField(max_length=50, null= True)
    phoneNumber = models.IntegerField(20,null= True)
    email = models.CharField(max_length=100)
    about = models.CharField(max_length=200,null= True)
    country = models.CharField(max_length=30, null= True)
    language = models.CharField(max_length=30, null= True)
    profilePicture = (models.ImageField(upload_to='profile_images',blank = True, null= True))
    
    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    postID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    postContent = models.CharField(max_length=1000)
    postImage = (models.ImageField(upload_to='images',blank = True))
    postDate = models.DateTimeField()
    postLikes = models.IntegerField(999)
    postBy = models.ForeignKey(UserAccount,on_delete=models.SET_NULL,null=True)
    likedBy = models.ManyToManyField(UserAccount, blank=True,related_name='liked_posts')

    

class Comment(models.Model):
    commentID = models.AutoField(primary_key=True)
    commentedBy = models.ForeignKey(UserAccount,on_delete=models.SET_NULL,null=True)
    commentOnPost = models.ForeignKey(Post,on_delete=models.SET_NULL,null=True)
    commentDate = models.DateTimeField()
    commentContent = models.CharField(max_length=50)