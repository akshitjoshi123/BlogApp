from django.shortcuts import render
from rest_framework import generics
from articles.serializers import ArticleCreateSerializer, ArticleSerializer
from articles.models import Article
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
