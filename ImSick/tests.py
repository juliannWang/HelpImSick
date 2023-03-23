from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from ImSick.models import UserAccount, Post, Comment
from django.utils import timezone
from django.http import JsonResponse
# Create your tests here.

def setUp(self):
        self.user = User.objects.create_user(username = 'testusername', password='testpassword')
        self.user_account = UserAccount.objects.create(
            user=self.user,
            name='Test User',
            phoneNumber=1234567890,
            email='fakeemail@gmail.com',
            about='This is a test user.',
            country='Test Country',
            language='Test Language'
        )
        self.client.login(username='testusername', password='testpassword')

class UserLogoutViewTest(TestCase):
    #test user can log out successfully
    def test_successful_user_logout(self):
        response = self.client.get(reverse('HelpImSick:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('HelpImSick:login'))

    def test_user_logged_in_before_logging_out(self):
        self.client.login(username='testusername', password='testpassword')
        response = self.client.get(reverse('HelpImSick:logout'))
        self.assertEqual(response.status_code, 302)
        user = authenticate(username='testusername', password='password')
        self.assertIsNone(user)

    def test_logout_redirects_to_login_page(self):
        self.client.login(username='testusername', password='testpassword')
        response = self.client.get(reverse('HelpImSick:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('HelpImSick:login'))

    def test_user_can_log_in_again_after_logging_out(self):
        self.client.login(username='testusername', password='testpassword')
        self.client.get(reverse('HelpImSick:logout'))
        self.client.login(username='testusername', password='testpassword')
        response = self.client.get(reverse('HelpImSick:test'))
        self.assertEqual(response.status_code, 302)

class IndexViewTest(TestCase):
    def setUp(self):
        self.client.login(username='testuser', password='testpass')
        self.url = reverse('HelpImSick:test')

    def test_logged_in_user_can_access_page(self):
        self.client.login(username='testusername', password='testpassword')
        response = self.client.get(reverse('HelpImSick:test'))
        self.assertEqual(response.status_code, 302)

    def test_context_data(self):
        self.client.login(username='testusername', password='testpassword')
        user = authenticate(username='testusername', password='password')
        post1 = Post.objects.create(title='Test Post 1', postContent='test content 1', postDate = timezone.now(), postLikes=0)
        post2 = Post.objects.create(title='Test Post 2', postContent='test content 2', postDate = timezone.now(), postLikes=0)

        comment1 = Comment.objects.create(commentedBy=user,commentOnPost=post1,commentDate = timezone.now(), commentContent="comment 1")
        comment2 = Comment.objects.create(commentedBy=user,commentOnPost=post2,commentDate = timezone.now(), commentContent="comment 2")

        posts=Post.objects.all()
        comments=Comment.objects.all()
        response = self.client.get(self.url)

        self.assertQuerysetEqual(response.context['posts'], posts)
        self.assertQuerysetEqual(response.context['comments', comments])

class UserLoginTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username = 'testusername', password='testpassword')
        self.user_account = UserAccount.objects.create(
            user=self.user,
            name='Test User',
            phoneNumber=1234567890,
            email='fakeemail@gmail.com',
            about='This is a test user.',
            country='Test Country',
            language='Test Language'
        )

    def test_valid_user_login(self):
        response = self.client.post(reverse('HelpImSick:login'), {'username': 'testusername', 'password': 'testpassword'})
        self.assertRedirects(response, reverse('HelpImSick:test'), status_code=302)

    def test_invalid_user_login(self):
        response = self.client.post(reverse('HelpImSick:login'), {'username': 'invaliduser', 'password': 'invalidpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Email or password incorrect")

class CreateAccountViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('HelpImSick:createAccount')

    def test_successful_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
    
    def test_successful_post_request(self):
        data = {
            'email' : 'fakeemail@gmail.com',
            'username': 'testusername',
            'password': 'testpassword'
        }
        response = self.client.post(self.url, data=data)
        self.assertRedirects(response, reverse('HelpImSick:login'))
        self.assertTrue(UserAccount.objects.filter(email='fakeemail@gmail.com').exists())

    def test_invalid_input_register(self):
        data = {
        'email': 'invalidemail', 
        'username': '', 
        'password': 'short'
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 302)


class MyPostsViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testusername',
            password='testpassword')
        self.user_account = UserAccount.objects.create(
            user=self.user,
            name='Test User',
            phoneNumber=1234567890,
            email='fakeemail@gmail.com',
            about='This is a test user.',
            country='Test Country',
            language='Test Language'
            )
        self.post = Post.objects.create(
            postBy=self.user_account,
            title = "post1",
            postContent = "post1content",
            postDate = timezone.now(),
            postLikes=0)

    def test_myPosts_view_returns_200_status_code(self):
        self.client.login(username='testusername', password='testpassword')
        url = reverse('HelpImSick:myPosts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_myPosts_view_uses_correct_template(self):
        self.client.login(username='testusername', password='testpassword')
        url = reverse('HelpImSick:myPosts')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'myPosts.html')

    def test_myPosts_view_returns_correct_context(self):
        self.client.login(username='testusername', password='testpassword')
        url = reverse('HelpImSick:myPosts')
        response = self.client.get(url)
        self.assertEqual(response.context['posts'].count(), 1)
        self.assertEqual(response.context['user'], self.user_account)
        self.assertEqual(response.context['favPosts'].count(), 0)

class TestCreatePostView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('HelpImSick:createPost')
        self.user = User.objects.create_user(username='testusername', password='testpassword')
        self.user_account = UserAccount.objects.create(
            user=self.user,
            name='Test User',
            phoneNumber=1234567890,
            email='fakeemail@gmail.com',
            about='This is a test user.',
            country='Test Country',
            language='Test Language'
        )
        self.form_data = {
            'postTitle': 'Test Post',
            'postContent': 'This is a test post.'
        }
        self.invalid_form_data = {
            'postTitle': 'post title',
            'postContent': 'This is a test post.',
        }

        def test_createPost_renders_template_with_form_if_authenticated_and_get_request(self):
            self.client.login(username='testusername', password='testpassword')
            response = self.client.get('HelpImSick:createPost')
            self.assertTemplateUsed(response, 'createPost.html')
            self.assertIsInstance(response.context['form'], PostForm)

        def test_authenticated_user_can_create_post_with_valid_data(self):
            response = self.client.post(self.url, self.form_data, follow=True)
            self.assertEqual(response.status_code, 200)
            self.assertRedirects(response, reverse('HelpImSick:test'))
            self.assertEqual(Post.objects.count(), 1)
            post = Post.objects.first()
            self.assertEqual(post.postTitle, 'Test Post')
            self.assertEqual(post.postBody, 'This is a test post.')
            self.assertEqual(post.postBy, UserAccount.objects.get(user=self.user))
            self.assertEqual(post.postLikes, 0)
            self.assertIsNotNone(post.postDate)
            self.assertIsNone(post.postImage)
        
        def test_invalid_form_submission_results_in_form_errors(self):
            response = self.client.post(self.url, self.invalid_form_data)
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'This field is required.')


class GetNearbyDoctorsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testusername',
            password='testpassword',
            email='fakeemail@gmail.com'
        )

    def test_get_nearby_doctors(self):
        url = reverse('HelpImSick:nearby-doctors')
        lat, lon = 55.860916, -4.251433 # Glasgow coordinates
        response = self.client.get(url, {'lat': lat, 'lon': lon}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 302)
        self.assertIsInstance(response, JsonResponse)

    def test_get_nearby_doctors_returns_3_doctors(self):
        url = reverse('HelpImSick:nearby-doctors')
        lat, lon = 55.860916, -4.251433 # Glasgow coordinates
        response = self.client.get(url, {'lat': lat, 'lon': lon}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 302)
        response_data = response.json()
        self.assertIsInstance(response_data, dict)
        self.assertEqual(len(response_data), 3)
        
   