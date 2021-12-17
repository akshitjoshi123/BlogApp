from django.contrib import admin
from accounts.models import User
from .models import Article, Categories, Comment
# Register your models here.

admin.site.register(User)
admin.site.register(Article)
admin.site.register(Categories)
admin.site.register(Comment)