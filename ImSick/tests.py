from django.urls import reverse
import importlib
from django.test import TestCase
from django.contrib.auth.models import User
from ImSick.models import UserAccount, Post, Comment
from datetime import datetime



class PostDetailsTests(TestCase):
    """
    Tests to check the postDetails view.
    We check whether the view exists, the mapping is correct, and the response is correct.
    """
    def setUp(self):
        self.views_module = importlib.import_module('ImSick.views')
        self.views_module_listing = dir(self.views_module)
    
    def test_view_exists(self):

        name_exists = 'postDetails' in self.views_module_listing
        is_callable = callable(self.views_module.about)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}We couldn't find the view for your postDetails view! It should be called postDetails().{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}Check you have defined your postDetails() view correctly. We can't execute it.{FAILURE_FOOTER}")
    
    def test_mapping_exists(self):
       
        self.assertEquals(reverse('HelpImSick:post'), 'post/<int:postID>', f"{FAILURE_HEADER}Your about URL mapping is either missing or mistyped.{FAILURE_FOOTER}")
    
    
class DeleteCommentTests(TestCase):  

    def test_view_exists(self):

        name_exists = 'deleteComment' in self.views_module_listing
        is_callable = callable(self.views_module.about)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}We couldn't find the view for your delete comment view! It should be called deleteComment().{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}Check you have defined your deleteComment() view correctly. We can't execute it.{FAILURE_FOOTER}")
    
    def test_mapping_exists(self):
       
        self.assertEquals(reverse('HelpImSick:post'), 'post/<int:postID>/deletecomment/<int:commentID>/', f"{FAILURE_HEADER}Your about URL mapping is either missing or mistyped.{FAILURE_FOOTER}")


class DeletePostTests(TestCase):  

    def test_view_exists(self):

        name_exists = 'deletePost' in self.views_module_listing
        is_callable = callable(self.views_module.about)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}We couldn't find the view for your delete post view! It should be called deletePost().{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}Check you have defined your deletePost() view correctly. We can't execute it.{FAILURE_FOOTER}")
    
    def test_mapping_exists(self):
       
        self.assertEquals(reverse('HelpImSick:myPosts'), 'post/<int:postID>/delete/', f"{FAILURE_HEADER}Your about URL mapping is either missing or mistyped.{FAILURE_FOOTER}")

class LikePostTests(TestCase):  

    def test_view_exists(self):

        name_exists = 'likePost' in self.views_module_listing
        is_callable = callable(self.views_module.about)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}We couldn't find the view for your like post view! It should be called likePost().{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}Check you have defined your likePost() view correctly. We can't execute it.{FAILURE_FOOTER}")
    
    def test_mapping_exists(self):
       
        self.assertEquals(reverse('HelpImSick:post'), 'post/<int:postID>/like/', f"{FAILURE_HEADER}Your about URL mapping is either missing or mistyped.{FAILURE_FOOTER}")


class favouritePostTests(TestCase):  

    def test_view_exists(self):

        name_exists = 'favouritePost' in self.views_module_listing
        is_callable = callable(self.views_module.about)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}We couldn't find the view for your favourite post view! It should be called favouritePost().{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}Check you have defined your favouritePost() view correctly. We can't execute it.{FAILURE_FOOTER}")
    
    def test_mapping_exists(self):
       
        self.assertEquals(reverse('HelpImSick:post'), 'post/<int:postID>/favPost/', f"{FAILURE_HEADER}Your about URL mapping is either missing or mistyped.{FAILURE_FOOTER}")

class unfavouritePostTests(TestCase):  

    def test_view_exists(self):

        name_exists = 'unfavouritePost' in self.views_module_listing
        is_callable = callable(self.views_module.about)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}We couldn't find the view for your unfavourite post view! It should be called unfavouritePost().{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}Check you have defined your unfavouritePost() view correctly. We can't execute it.{FAILURE_FOOTER}")
    
    def test_mapping_exists(self):
       
        self.assertEquals(reverse('HelpImSick:post'), 'post/<int:postID>/unfavPost/', f"{FAILURE_HEADER}Your about URL mapping is either missing or mistyped.{FAILURE_FOOTER}")

class unlikePostTests(TestCase):  

    def test_view_exists(self):

        name_exists = 'unlikePost' in self.views_module_listing
        is_callable = callable(self.views_module.about)
        
        self.assertTrue(name_exists, f"{FAILURE_HEADER}We couldn't find the view for your unlike post view! It should be called unlikePost().{FAILURE_FOOTER}")
        self.assertTrue(is_callable, f"{FAILURE_HEADER}Check you have defined your likePost() view correctly. We can't execute it.{FAILURE_FOOTER}")
    
    def test_mapping_exists(self):
       
        self.assertEquals(reverse('HelpImSick:post'), 'post/<int:postID>/unlike/', f"{FAILURE_HEADER}Your about URL mapping is either missing or mistyped.{FAILURE_FOOTER}")

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
