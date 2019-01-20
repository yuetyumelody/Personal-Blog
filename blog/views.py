from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Post
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutMeView(TemplateView):
    template_name = 'aboutme.html'

class BlogListView(ListView):
    model = Post
    template_name = 'blog_home.html'
    context_object_name = 'blog_list'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class RecipeListView(ListView):
    model = Post
    template_name = 'recipe_list.html'
    context_object_name = 'recipe_list'

class RecipeDetailView(DetailView):
    model = Post
    temaplate_name = 'recipe_detail.html'