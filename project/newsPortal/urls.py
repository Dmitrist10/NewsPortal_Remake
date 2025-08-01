from django.contrib import admin
from django.urls import include, path
from .views import PostsList, PostDetail, NewsList, ArticlsList


urlpatterns = [
    path('posts/', PostsList.as_view(), name='posts_list'),
    path('posts/<int:pk>', PostDetail.as_view()),
    path('news/', NewsList.as_view(), name='news_list'),
    path('articles/', ArticlsList.as_view(), name='articles_list'),
]