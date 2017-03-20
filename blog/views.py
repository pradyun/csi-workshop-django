from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone

from blog.forms import PostForm,SignUpForm

from .models import Category,Blog

# Create your views here.

@login_required(login_url="login/")
def index(request):
    cat = Category.objects.all()
    posts = Blog.objects.all()[:5]
    return render(request,'index.html', {
        'categories': cat,
        'posts': posts
    })

@login_required(login_url="login/")
def view_post(request,id):
    post = Blog.objects.get(pk=id)
    return render(request,'post.html', {
        'post': post
    })

@login_required(login_url="login/")
def view_category(request, id):
    cat = Category.objects.get(pk=id)
    posts = Blog.objects.filter(category=cat)[:5]
    return render(request,'category.html', {
        'category': cat,
        'posts': posts
    })

@login_required(login_url="login/")
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            post.author = request.user
            post.posted = timezone.now()
            post.category =  Category.objects.get(title='Default')
            post.save()

            return HttpResponseRedirect('/blog')
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form': form})

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email'])
            return HttpResponseRedirect('/blog')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})
