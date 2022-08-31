from django.urls import path
from .views import CulBlog, BlogDetailView, AddBlogView

urlpatterns = [
    path('', CulBlog.as_view(), name="blog"),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(), name="blog_detail"),
    path('add_blog/', AddBlogView.as_view(), name="add_blog"),
]