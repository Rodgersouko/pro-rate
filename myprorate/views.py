from django.shortcuts import render, redirect
from .forms import SignupForm, PostForm
from django.contrib.auth import login, authenticate
from rest_framework import viewsets
from .models import Profile, Post
from .serializers import ProfileSerializer
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            post.user = request.user.profile
    else:
        form = PostForm()

    try:
        posts = Post.objects.all()
        print(posts)
    except Post.DoesNotExist:
        posts = None
    return render(request, 'index.html', {'posts': posts, 'form':form})



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def profile(request, username):
    return render(request, 'profile.html')


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    print(queryset)
    serializer_class = ProfileSerializer


def project(request, post):
    post = Post.objects.get(title=post)

    params = {
        'post': post
    }
    return render(request, 'project.html', params)
