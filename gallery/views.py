from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import Image


def index(request):
    return redirect('news/')


def news_index(request):
    return redirect('1/')


def news(request, page_number):
    show_posts = 50 # how many posts are going to be shown at one page
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    queryset = Image.objects.all()[::-1]
    context = {
        'username': username,
        'images': queryset,
    }
    return render(request, 'news.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'username': username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'profile_picture': None,
        'email': user.email,
    }
    return render(request, 'profile.html', context)
