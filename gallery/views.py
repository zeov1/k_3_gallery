from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import Image


def index(request):
    return redirect('news_index')


def news_index(request):
    return redirect('news', '1')


def news(request, page_number):
    if page_number < 1:
        return redirect('news', '1')
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True
        context['username'] = request.user.username
    else:
        context['is_authenticated'] = False

    show_posts = 15  # how many posts are going to be shown at one page
    first_post_number = show_posts * (page_number - 1)
    context['images'] = Image.objects.all()[::-1][first_post_number:show_posts + first_post_number]
    return render(request, 'news.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'profile_picture': None,
        'email': user.email,
    }
    if request.user.is_authenticated:
        context['is_authenticated'] = True
        context['username'] = request.user.username
    else:
        context['is_authenticated'] = False
    return render(request, 'profile.html', context)
