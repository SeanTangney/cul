from django.views.generic import ListView, DetailView
from .models import Post


class CulBlog(ListView):
    model = Post
    template_name = 'blog/blog.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
