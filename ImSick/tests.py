import datetime
from django.utils import timezone
from django.urls import reverse
import importlib
from django.test import TestCase
from django.contrib.auth.models import User
from ImSick.models import UserAccount, Post, Comment
from datetime import datetime


from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from ImSick.models import Post, Comment, UserAccount

#tests for views

class PostDetailsTests(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user_account = UserAccount.objects.create(
            user=self.user,
            name='Test User',
            phoneNumber=1234567890,
            email='test@example.com',
            about='This is a test user.',
            country='Test Country',
            language='Test Language'
        )
        self.post = Post.objects.create(
            title='Test Post',
            postContent='This is a test post.',
            postDate=timezone.now(),
            postLikes=0,
            postBy=self.user_account
        )
        self.comment = Comment.objects.create(
            commentedBy=self.user_account,
            commentOnPost=self.post,
            commentDate=timezone.now(),
            commentContent='This is a test comment.',
            commentID=1
        )
        self.postID = 1
        self.url = reverse('HelpImSick:post',
                           args=[self.postID])
        
    def tests_post_details(self):
        self.client.login(username='testuser', password='testpass')
        self.client.post(self.url)
        self.assertEquals(self.comment.commentID, 1)
        self.assertEquals(self.post.postContent, 'This is a test post.') 
        self.assertEquals(self.user_account.name,'Test User' ) 

 

   
class DeleteCommentTests(TestCase):  

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user_account = UserAccount.objects.create(
            user=self.user,
            name='Test User',
            phoneNumber=1234567890,
            email='test@example.com',
            about='This is a test user.',
            country='Test Country',
            language='Test Language'
        )
        self.post = Post.objects.create(
            title='Test Post',
            postContent='This is a test post.',
            postDate=timezone.now(),
            postLikes=0,
            postBy=self.user_account
        )
        self.comment = Comment.objects.create(
            commentedBy=self.user_account,
            commentOnPost=self.post,
            commentDate=timezone.now(),
            commentContent='This is a test comment.',
            commentID=1
        )
        self.postID = 1
        self.commentID = 1
        self.url = reverse('HelpImSick:deleteComment',
                           args=[self.postID, self.commentID])
        
        
    def tests_delete_comment(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.url)
        self.assertFalse(Comment.objects.filter(commentID=self.commentID).exists())



class DeletePostTests(TestCase):  

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user_account = UserAccount.objects.create(
            user=self.user,
            name='Test User',
            phoneNumber=1234567890,
            email='test@example.com',
            about='This is a test user.',
            country='Test Country',
            language='Test Language'
        )
        self.post = Post.objects.create(
            title='Test Post',
            postContent='This is a test post.',
            postDate=timezone.now(),
            postLikes=0,
            postBy=self.user_account
        )
        self.comment = Comment.objects.create(
            commentedBy=self.user_account,
            commentOnPost=self.post,
            commentDate=timezone.now(),
            commentContent='This is a test comment.',
            commentID=1
        )
        self.postID = 1
        self.commentID = 1
        self.url = reverse('HelpImSick:deletePost',
                           args=[self.postID])
        
        
    def tests_delete_posts(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.url)
        self.assertFalse(Post.objects.filter(postID=self.postID).exists())

class LikePostTests(TestCase):  

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user_account = UserAccount.objects.create(
            user=self.user,
            name='Test User',
            phoneNumber=1234567890,
            email='test@example.com',
            about='This is a test user.',
            country='Test Country',
            language='Test Language'
        )
        self.post = Post.objects.create(
            title='Test Post',
            postContent='This is a test post.',
            postDate=timezone.now(),
            postLikes=0,
            postBy=self.user_account
        )
        self.comment = Comment.objects.create(
            commentedBy=self.user_account,
            commentOnPost=self.post,
            commentDate=timezone.now(),
            commentContent='This is a test comment.',
            commentID=1
        )
        self.postID = 1
        self.commentID = 1
        self.post.postLikes+=1
        self.url = reverse('HelpImSick:likePost',
                           args=[self.postID])
        
        
    def tests_like_post(self):
        self.client.login(username='testuser', password='testpass')
        self.client.post(self.url)
        self.assertEqual(self.post.postLikes, 1)
    


class favouritePostTests(TestCase):  

    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user_account = UserAccount.objects.create(
            user=self.user,
            name='Test User',
            phoneNumber=1234567890,
            email='test@example.com',
            about='This is a test user.',
            country='Test Country',
            language='Test Language'
        )
        self.post = Post.objects.create(
            title='Test Post',
            postContent='This is a test post.',
            postDate=timezone.now(),
            postLikes=1,
            postBy=self.user_account,
            
        )
        self.comment = Comment.objects.create(
            commentedBy=self.user_account,
            commentOnPost=self.post,
            commentDate=timezone.now(),
            commentContent='This is a test comment.',
            commentID=1
        )
        self.postID = 1
        self.commentID = 1
        self.user_account.favoritePosts.add(self.post)
        self.url = reverse('HelpImSick:favPost',
                           args=[self.postID])
        
        
        
    def tests_favourite_post(self):
        self.client.login(username='testuser', password='testpass')
        self.client.post(self.url)
        self.assertTrue(self.post in self.user_account.favoritePosts.all())

class unfavouritePostTests(TestCase):  

    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user_account = UserAccount.objects.create(
            user=self.user,
            name='Test User',
            phoneNumber=1234567890,
            email='test@example.com',
            about='This is a test user.',
            country='Test Country',
            language='Test Language'
        )
        self.post = Post.objects.create(
            title='Test Post',
            postContent='This is a test post.',
            postDate=timezone.now(),
            postLikes=1,
            postBy=self.user_account
        )
        self.comment = Comment.objects.create(
            commentedBy=self.user_account,
            commentOnPost=self.post,
            commentDate=timezone.now(),
            commentContent='This is a test comment.',
            commentID=1
        )
        self.postID = 1
        self.commentID = 1
        self.url = reverse('HelpImSick:unfavPost',
                           args=[self.postID])
        
        
    def tests_unfavourite_post(self):
        self.client.login(username='testuser', password='testpass')
        self.client.post(self.url)
        self.assertFalse(self.post in self.user_account.favoritePosts.all())

class unlikePostTests(TestCase):  

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user_account = UserAccount.objects.create(
            user=self.user,
            name='Test User',
            phoneNumber=1234567890,
            email='test@example.com',
            about='This is a test user.',
            country='Test Country',
            language='Test Language'
        )
        self.post = Post.objects.create(
            title='Test Post',
            postContent='This is a test post.',
            postDate=timezone.now(),
            postLikes=1,
            postBy=self.user_account
        )
        self.comment = Comment.objects.create(
            commentedBy=self.user_account,
            commentOnPost=self.post,
            commentDate=timezone.now(),
            commentContent='This is a test comment.',
            commentID=1
        )
        self.postID = 1
        self.commentID = 1
        self.post.postLikes-=1
        self.url = reverse('HelpImSick:unlikePost',
                           args=[self.postID])
        
        
    def tests_unlike_post(self):
        self.client.login(username='testuser', password='testpass')
        self.client.post(self.url)
        self.assertEqual(self.post.postLikes, 0)

# tests for models

class UserAccountTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user_account = UserAccount.objects.create(
            user=self.user,
            name='Test User',
            phoneNumber=1234567890,
            email='test@example.com',
            about='This is a test user.',
            country='Test Country',
            language='Test Language'
        )

    def test_user_account_str(self):
        self.assertEqual(str(self.user_account), self.user.username)

    def test_user_account_attributes(self):
        self.assertEqual(self.user_account.name, 'Test User')
        self.assertEqual(self.user_account.phoneNumber, 1234567890)
        self.assertEqual(self.user_account.email, 'test@example.com')
        self.assertEqual(self.user_account.about, 'This is a test user.')
        self.assertEqual(self.user_account.country, 'Test Country')
        self.assertEqual(self.user_account.language, 'Test Language')

class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user_account = UserAccount.objects.create(
            user=self.user,
            name='Test User',
            phoneNumber=1234567890,
            email='test@example.com',
            about='This is a test user.',
            country='Test Country',
            language='Test Language'
        )
        self.post = Post.objects.create(
            title='Test Post',
            postContent='This is a test post.',
            postDate=datetime.now(),
            postLikes=0,
            postBy=self.user_account
        )

    def test_post_attributes(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.postContent, 'This is a test post.')
        self.assertEqual(self.post.postLikes, 0)
        self.assertEqual(self.post.postBy, self.user_account)


class CommentTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user_account = UserAccount.objects.create(
            user=self.user,
            name='Test User',
            phoneNumber=1234567890,
            email='test@example.com',
            about='This is a test user.',
            country='Test Country',
            language='Test Language'
        )
        self.post = Post.objects.create(
            title='Test Post',
            postContent='This is a test post.',
            postDate=datetime.now(),
            postLikes=0,
            postBy=self.user_account
        )
        self.comment = Comment.objects.create(
            commentedBy=self.user_account,
            commentOnPost=self.post,
            commentDate=datetime.now(),
            commentContent='This is a test comment.'
        )

    def test_comment_attributes(self):
        self.assertEqual(self.comment.commentedBy, self.user_account)
        self.assertEqual(self.comment.commentOnPost, self.post)
        self.assertEqual(self.comment.commentContent, 'This is a test comment.')
