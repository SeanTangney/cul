from django.urls import path
from .views import CulBlog, BlogDetailView, AddBlogView, UpdateBlogView, DeleteBlogView

urlpatterns = [
    path('', CulBlog.as_view(), name="blog"),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(), name="blog_detail"),
    path('add/', AddBlogView.as_view(), name="add_blog"),
    path('blog-detail/update/<int:pk>', UpdateBlogView.as_view(), name="update_blog"),
    path('blog-detail/detail/<int:pk>', DeleteBlogView.as_view(), name="delete_blog"),
]
