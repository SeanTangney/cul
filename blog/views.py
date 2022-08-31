from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm


class CulBlog(ListView):
    model = Post
    template_name = 'blog/blog.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'


class AddBlogView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_blog.html'
