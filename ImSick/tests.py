from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import datetime
from .models import Post, Comment, UserAccount

# tests for models and last 3 views

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
    

    def test_user_account_profile_picture(self):
        from django.core.files.uploadedfile import SimpleUploadedFile
        # create a fake image file to use for testing
        fake_image = SimpleUploadedFile("fake_image.png", b"file_content", content_type="image/png")
        self.user_account.profilePicture = fake_image
        self.user_account.save()
        # retrieve the saved image file
        saved_image = UserAccount.objects.get(pk=self.user_account.pk).profilePicture
        self.assertIsNotNone(saved_image)



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


    def test_post_liked_by_users(self):
        user2 = User.objects.create_user(username='testuser2', password='testpass')
        user_account2 = UserAccount.objects.create(
            user=user2,
            name='Test User 2',
            phoneNumber=1234567890,
            email='test2@example.com',
            about='This is another test user.',
            country='Test Country',
            language='Test Language'
        )
        self.post.likedBy.add(self.user_account)
        self.post.likedBy.add(user_account2)
        self.assertEqual(list(self.post.likedBy.all()), [self.user_account, user_account2])
    
    def test_post_post_image(self):
        from django.core.files.uploadedfile import SimpleUploadedFile
        # create a fake image file to use for testing
        fake_image = SimpleUploadedFile("fake_image.png", b"file_content", content_type="image/png")
        self.post.postImage = fake_image
        self.post.save()
        # retrieve the saved image file
        saved_image = Post.objects.get(pk=self.post.pk).postImage
        self.assertIsNotNone(saved_image)



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

class SettingsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.user_account = UserAccount.objects.create(user=self.user)
        self.client.login(username='testuser', password='password')

    def test_settings_page_renders(self):
        response = self.client.get(reverse('HelpImSick:settings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'settings.html')

    def test_settings_updates_user_account(self):
        response = self.client.post(reverse('HelpImSick:settings'), {
            'name': 'New Name',
            'phoneNumber': '1234567890',
            'email': 'new_email@example.com',
            'about': 'New About',
            'country': 'New Country',
            'language': 'New Language',
        })
        self.assertEqual(response.status_code, 302)
        updated_user_account = UserAccount.objects.get(user=self.user)
        self.assertEqual(updated_user_account.name, 'New Name')
        self.assertEqual(updated_user_account.phoneNumber, '1234567890')
        self.assertEqual(updated_user_account.email, 'new_email@example.com')
        self.assertEqual(updated_user_account.about, 'New About')
        self.assertEqual(updated_user_account.country, 'New Country')
        self.assertEqual(updated_user_account.language, 'New Language')


class ViewProfileTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.user_account = UserAccount.objects.create(user=self.user, name='Test User')
       


    def test_view_own_profile(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse("HelpImSick:viewProfile", args=[self.user_account.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user_account.name)
    
    def test_view_other_profile(self):
        other_user = User.objects.create_user(username='otheruser', password='password')
        other_user_account = UserAccount.objects.create(user=other_user, name='Other Name')
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('HelpImSick:viewProfile', args=[other_user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, other_user_account.name)

class SearchPostsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.user_account = UserAccount.objects.create(user=self.user)
        self.post1 = Post.objects.create(title='Test Post 1', postContent='This is a test post 1', postBy=self.user_account)
        self.post2 = Post.objects.create(title='Test Post 2', postContent='This is a test post 2', postBy=self.user_account)
        self.post3 = Post.objects.create(title='Another Post', postContent='This is another test post', postBy=self.user_account)

    def test_search_posts_with_title(self):
        response = self.client.get(reverse('HelpImSick:search'), {'query': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post2.title)
        self.assertNotContains(response, self.post3.title)

    def test_search_posts_with_content(self):
        response = self.client.get(reverse('HelpImSick:search'), {'query': 'another'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post3.title)
        self.assertNotContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_search_posts_with_invalid_query(self):
        response = self.client.get(reverse('HelpImSick:search'), {'query': 'invalid'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No posts found.')

