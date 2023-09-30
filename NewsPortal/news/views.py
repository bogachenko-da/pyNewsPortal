from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime


class NewsList(ListView):
    model = Post
    ordering = '-post_created'
    template_name = 'news.html'
    context_object_name = 'news'


class PostList(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
