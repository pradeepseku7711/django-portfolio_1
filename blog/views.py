from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404
from .models import project_blog

# Create your views here.
def all_blog(request):
    blogs=project_blog.objects.order_by('-date')[:5]
    return render(request,'blog/all_blog.html',{'blogs':blogs})

def detail(request,blog_id):
    blog = get_object_or_404(project_blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog': blog})