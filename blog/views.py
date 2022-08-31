from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class CulBlog(ListView):
    model = Post
    template_name = 'blog/blog.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'


class AddBlogView(CreateView):
    model = Post
    template_name = 'blog/add_blog.html'
    fields = '__all__'
