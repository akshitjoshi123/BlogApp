from django.db import models
from accounts.models import User

# Create your models here.
STATUS = (
    ("draft", "draft"),
    ("publish", "publish"),
)


class Categories(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()

    def __str__(self):
        return self.title


class Article(models.Model):
    """article model for article to create, update, list"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Categories)
    status = models.CharField(choices=STATUS, max_length=20)
    image = models.ImageField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    """comment model to comment a message on article"""
    comment = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default='Anonymous Users')
    

    def __str__(self):
        return self.name