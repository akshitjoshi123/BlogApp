from re import search
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics
from articles.serializers import ArticleCreateSerializer, ArticleSerializer, CategorySerializer, CommentSerializer, CommentListSerializer
from articles.models import Article, Categories, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import filters
from .pagination import CustomPagination

# Create your views here.



class ArticleCreateApi(LoginRequiredMixin, generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserArticleListApi(LoginRequiredMixin, generics.ListAPIView):
    serializer_class = ArticleCreateSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title']
    pagination_class = CustomPagination

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)


class ArticleUpdateApi(LoginRequiredMixin, generics.RetrieveUpdateAPIView):
    serializer_class = ArticleCreateSerializer

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)


class ArticleDeleteApi(LoginRequiredMixin, generics.DestroyAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.all()


class GeneralArticleListApi(generics.ListAPIView):
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__first_name']
    ordering_fields = ['category', 'title']
    pagination_class = CustomPagination

    def get_queryset(self):
        return Article.objects.filter(status="publish").order_by('-id')


class CategoriesListApi(generics.ListAPIView):
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title']

    def get_queryset(self):
        return Categories.objects.all()


class ArticleCategoryList(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        categories = self.kwargs['pk']
        return Article.objects.filter(category__pk=categories, status='publish')


class CommentCreateApi(generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all() 

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(name=self.request.user)


class CommentListApi(generics.ListAPIView):
    serializer_class = CommentListSerializer

    def get_queryset(self):
        return Comment.objects.all().order_by('-id')
