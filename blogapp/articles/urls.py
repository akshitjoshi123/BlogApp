from django.urls import path
from articles.views import ArticleCreateApi, UserArticleListApi, ArticleUpdateApi, ArticleDeleteApi, GeneralArticleListApi, CategoriesListApi, ArticleCategoryList

urlpatterns = [
    path('create/', ArticleCreateApi.as_view()),
    path('list/', UserArticleListApi.as_view()),
    path('list/<int:pk>/', ArticleUpdateApi.as_view()),
    path('list/delete/<int:pk>/', ArticleDeleteApi.as_view()),
    path('',GeneralArticleListApi.as_view()),
    path('categories/', CategoriesListApi.as_view()),
    path('categories/<int:pk>/', ArticleCategoryList.as_view()),
]