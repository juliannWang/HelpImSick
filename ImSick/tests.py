from django.test import TestCase

# tests for models

from django.contrib.auth.models import User
from ImSick.models import UserAccount, Post, Comment
from datetime import datetime

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