from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


class CulBlog(ListView):
    model = Post
    template_name = 'blog/blog.html'
    ordering = ['-post_on']


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'


class AddBlogView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_blog.html'


class UpdateBlogView(UpdateView):
    model = Post
    template_name = 'blog/update_blog.html'
    fields = [
        'image',
        'title',
        'body',
    ]


class DeleteBlogView(DeleteView):
    model = Post
    template_name = 'blog/delete_blog.html'
    success_url = reverse_lazy('blog')
