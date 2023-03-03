import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HelpImSick.settings")
import django
django.setup()
from ImSick.models import UserAccount, Post, Comment
from django.contrib.auth.models import User
from faker import Faker
import csv
import random


def populate():
    createFiveRandomAccounts()
    createFakePostsAndComments()


def createFiveRandomAccounts():
    fake = Faker()
    details = []
    for i in range(5):
        username = fake.user_name()
        password = fake.password()
        email = fake.email()
        user = User.objects.get_or_create(username=username,email=email)[0]
        user.set_password(password)
        user.save()
        
        name = fake.name()
        phonenumber= "0000000000"
        about = fake.text()
        country = fake.country()
        language = "english"
        user_account = UserAccount.objects.get_or_create(user = user, name = name,phoneNumber = phonenumber,about = about , country = country ,language = language,email=email)[0]
        user_account.save()
        userdetails = []
        userdetails = [username,password,email,name]
        details.append(userdetails)
    exportaccounts(details)
    
def exportaccounts(details):
    with open("useraccount_details_output","w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(details)
        
def createFakePostsAndComments():
    fake = Faker()
    user_accounts = UserAccount.objects.all()
    user_ids = [account.user_id for account in user_accounts]
    
    for i in range(5):
        title = fake.sentence()
        postContent = fake.text()
        postDate = fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)
        postLikes = 0
        postBy = UserAccount.objects.filter(user_id = user_ids[i])[0]
        post = Post.objects.get_or_create(title=title,postContent=postContent,postDate=postDate,postLikes=postLikes,postBy=postBy)[0]
        post.save()
        
        for i in range(5):
            commentedBy = UserAccount.objects.filter(user_id = user_ids[random.randint(0,4)])[0]
            commentOnPost = post
            commentDate = fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)
            commentContext = fake.text()
            comment = Comment.objects.get_or_create(commentedBy = commentedBy,commentOnPost = commentOnPost,commentDate = commentDate,commentContent = commentContext)[0]
            comment.save()
    
    

if __name__ == "__main__":
    print("Starting population script...")
    populate()
    print("Completed population script, exiting...")

    
        
    
    
