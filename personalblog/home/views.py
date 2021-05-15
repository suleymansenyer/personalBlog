from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Blog

def blogs(request):
    data = Blog.objects.all()[::-1]
    p = Paginator(data, 3)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    data = {'data':page_obj,'page_obj': page_obj}
    return render(request,'blog.html',data)


def blog(request,blog_name):
    print(blog_name)
    data = Blog.objects.filter(blog_title = blog_name)[0]
    data = {'data': data}
    return render(request,'read.html',data)
