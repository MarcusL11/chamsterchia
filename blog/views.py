import markdown
from django.shortcuts import render, get_object_or_404
from .models import MarkdownContent

# Create your views here.

def blog(request, slug):
    markdown_content = get_object_or_404(MarkdownContent, slug=slug)
    context = {"markdown_content": markdown_content}
    return render(request,"blog/blog.html",context=context)