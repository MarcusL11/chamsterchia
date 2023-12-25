from django.urls import path
from . import views

urlpatterns = [
    path("blog/", views.blogHome, name="blog"),
    path("blog/<slug:slug>/", views.blog, name="blog-content",),    
]
