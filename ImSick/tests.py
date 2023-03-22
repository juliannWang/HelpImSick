from django.urls import reverse
import importlib
from django.test import TestCase


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


