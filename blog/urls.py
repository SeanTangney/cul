from django.urls import path
from .views import CulBlog, BlogDetailView

urlpatterns = [
    path('', CulBlog.as_view(), name="blog"),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(), name="blog_detail"),
]
