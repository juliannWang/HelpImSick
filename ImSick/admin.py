from django.contrib import admin
from ImSick.models import UserAccount, Post, Comment

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(Post)
admin.site.register(Comment)
