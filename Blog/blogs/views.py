from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogForm


def index(request):
    """博客主页"""
    return render(request, 'blogs/index.html')


@login_required
def title(request):
    """主题"""
    blogs = BlogPost.objects.filter(owner=request.user).order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/title.html', context)


@login_required
def new_blog(request):
    """新建主题"""
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            check_title_owner(request, blog)
            blog.save()
            return redirect('blogs:title')

    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)


@login_required
def edit_blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    check_title_owner(request, blog)
    if request.method != 'POST':
        form = BlogForm(instance=blog)
    else:
        form = BlogForm(instance=blog, data=request.POST)
        form.save()
        return redirect('blogs:title')

    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)


def check_title_owner(request, blog):
    """核实用户"""
    if blog.owner != request.user:
        raise Http404
