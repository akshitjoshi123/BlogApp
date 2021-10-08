from django.db import models
from django.db.models import fields
from rest_framework import serializers
from articles.models import Article, Categories, Comment


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'category', 'status', 'image']


class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.first_name')

    class Meta:
        model = Article
        fields = ['title', 'author_name', 'content', 'category', 'image']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['title', 'image']


class CommentSerializer(serializers.ModelSerializer):
    article = serializers.PrimaryKeyRelatedField(queryset=Article.objects.filter(status='publish'))

    class Meta:
        model = Comment
        fields = ['article', 'comment']


class CommentListSerializer(serializers.ModelSerializer):
    article_name = serializers.CharField(source='article.title')

    class Meta:
        model = Comment
        fields = ['name', 'article_name', 'comment']

