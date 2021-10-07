from django.urls import path
from articles.views import ArticleCreateApi, UserArticleListApi, ArticleUpdateApi, ArticleDeleteApi,GeneralArticleListApi

urlpatterns = [
    path('create/', ArticleCreateApi.as_view()),
    path('list/', UserArticleListApi.as_view()),
    path('list/<int:pk>/', ArticleUpdateApi.as_view()),
    path('list/delete/<int:pk>/', ArticleDeleteApi.as_view()),
    path('',GeneralArticleListApi.as_view()),

]