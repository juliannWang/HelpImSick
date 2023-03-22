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
    addRealTestData()


def addRealTestData():
    title1 = "Red Rash"
    post_content1 = "I have recently noticed a red rash on the side of my face, I have had it for about a week. Should I see a doctor?\nThis may be rosacea, although check with your doctor before trying to treat it"
    comment_1 = "Have you had any rashes like this before?"
    comment_2 = "Is it painful?"
    comment_3 = "Yes, it's always best to check with a doctor when you notice any unusual changes in your skin."

    
    title2 = "Broken Finger Surgery"
    post_content2 = "Hi, I broke my finger and recently had surgery on it. How long will it be before it is back to normal?"
    comment_4 = "Broken fingers typically heal in between 6 to 8 weeks, but it may be slightly longer if you've had surgery."
    comment_5 = "As the poster above said, around 6 to 8 weeks. You will also need to learn to write again and do any other activities you aren't able to currently."
    comment_6 = "It will depend on what type of surgery you had and what type of fracture."

    
    title3 = "Sprained ankle when I was younger"
    post_content3 = "I sprained my ankle when I was a teenager and have never recovered full range of motion in it. What can I do about this?"
    comment_7 = "See your doctor, you may be able to get surgery to restore it."
    comment_8 = "There are surgeries that can help you, although since you didn't receive it immediately, surgery might not fully help your ankle."
    comment_9 = "You probably should have seen a doctor when you sprained it."

    
    email="TestUser1Email@email.com"
    user1 = User.objects.get_or_create(username="TestUser1",email=email)[0]
    user1.set_password("TestUser1Password")
    user1.save()
    fake = Faker()
    name = fake.name()
    phonenumber = 91413386895
    about = "Hello I am just a friendly person who loves food"
    country = fake.country()
    language = "English"
    userAccount1 = UserAccount.objects.get_or_create(user = user1 , name = name,phoneNumber = phonenumber,about = about , country = country ,language = language,email=email)[0]
    
    email="user2@email.com"
    user2 = User.objects.get_or_create(username="User2",email=email)[0]
    user2.set_password("User2Password")
    user2.save()
    fake = Faker()
    name = fake.name()
    phonenumber = "91211234567"
    about = "I am an adventurous person who loves to travel."
    country = fake.country()
    language = "English"
    userAccount2 = UserAccount.objects.get_or_create(user=user2, name=name, phoneNumber=phonenumber, about=about, country=country, language=language, email=email)[0]
    
    email="user3@email.com"
    user3 = User.objects.get_or_create(username="User3",email=email)[0]
    user3.set_password("User3Password")
    user3.save()
    fake = Faker()
    name = fake.name()
    phonenumber = "092075551234"
    about = "I am a creative person who enjoys making things with my hands."
    country = fake.country()
    language = "English"
    userAccount3 = UserAccount.objects.get_or_create(user=user3, name=name, phoneNumber=phonenumber, about=about, country=country, language=language, email=email)[0]
    
    email="user4@email.com"
    user4 = User.objects.get_or_create(username="User4",email=email)[0]
    user4.set_password("User4Password")
    user4.save()
    fake = Faker()
    name = fake.name()
    phonenumber = "9028 1234 5678"
    about = "I am a book lover who enjoys reading in my spare time."
    country = fake.country()
    language = "English"
    userAccount4 = UserAccount.objects.get_or_create(user=user4, name=name, phoneNumber=phonenumber, about=about, country=country, language=language, email=email)[0]



    postDate = fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)
    post1 = Post.objects.get_or_create(title=title1,postContent=post_content1,postDate=postDate,postLikes=0,postBy=userAccount1)[0]
    post1.save()
    comment1 = Comment.objects.get_or_create(commentedBy = userAccount2,commentOnPost = post1,commentDate = fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None),commentContent = comment_1)[0]
    comment2 = Comment.objects.get_or_create(commentedBy = userAccount3,commentOnPost = post1,commentDate = fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None),commentContent = comment_2)[0]
    comment3 = Comment.objects.get_or_create(commentedBy = userAccount4,commentOnPost = post1,commentDate = fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None),commentContent = comment_3)[0]
    comment1.save()
    comment2.save()
    comment3.save()
    
    post2 = Post.objects.get_or_create(title=title2,postContent=post_content2,postDate=postDate,postLikes=0,postBy=userAccount1)[0]
    post2.save()
    comment4 = Comment.objects.get_or_create(commentedBy = userAccount2,commentOnPost = post2,commentDate = fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None),commentContent = comment_4)[0]
    comment5 = Comment.objects.get_or_create(commentedBy = userAccount3,commentOnPost = post2,commentDate = fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None),commentContent = comment_5)[0]
    comment6 = Comment.objects.get_or_create(commentedBy = userAccount4,commentOnPost = post2,commentDate = fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None),commentContent = comment_6)[0]
    comment4.save()
    comment5.save()
    comment6.save()

    post3 = Post.objects.get_or_create(title=title3,postContent=post_content3,postDate=postDate,postLikes=0,postBy=userAccount2)[0]
    post3.save()
    comment7 = Comment.objects.get_or_create(commentedBy = userAccount1,commentOnPost = post3,commentDate = fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None),commentContent = comment_7)[0]
    comment8 = Comment.objects.get_or_create(commentedBy = userAccount3,commentOnPost = post3,commentDate = fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None),commentContent = comment_8)[0]
    comment9 = Comment.objects.get_or_create(commentedBy = userAccount4,commentOnPost = post3,commentDate = fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None),commentContent = comment_9)[0]
    comment7.save()
    comment8.save()
    comment9.save()




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

    
        
    
    
