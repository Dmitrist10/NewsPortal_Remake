import datetime
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
class PostsList(ListView):
    model = Post
    template_name = 'NewsPortal/posts.html'
    context_object_name = 'posts'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.datetime.now()
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'NewsPortal/PostDetailsBase.html'
    context_object_name = 'post'
    # pk_url_kwarg = 'pk'




class NewsList(ListView):
    model = Post
    template_name = 'NewsPortal/news.html'
    context_object_name = 'news'
    queryset = Post.objects.filter(postType='NW')
    ordering = ['-creationDate']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.datetime.now()
        return context
    
class ArticlsList(ListView):
    model = Post
    template_name = 'NewsPortal/articles.html'
    context_object_name = 'articles'
    queryset = Post.objects.filter(postType='AR')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.datetime.now()
        return context
