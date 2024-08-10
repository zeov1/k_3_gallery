from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from .models import Image


def index(request):
    return redirect('news_index')


def news_index(request):
    return redirect('news', '1')


def news(request):
    page_number = request.GET.get('page_number', 1)
    try:
        page_number = int(page_number)
    except ValueError:
        return HttpResponseNotFound(f'Page {page_number} does not exist')
    if page_number < 1:
        page_number = 1
    context = {}

    show_posts = request.GET.get('show_posts', 15)
    first_post_number = show_posts * (page_number - 1)
    queryset = Image.objects.all()
    context['images'] = queryset[::-1][first_post_number:show_posts + first_post_number]

    length = len(queryset)
    max_page = (length + show_posts) // show_posts
    context['max_page'] = max_page
    context['page_number'] = page_number
    if page_number > 1:
        context['prev_page'] = page_number - 1
    if page_number < max_page:
        context['next_page'] = page_number + 1
    return render(request, 'gallery/news.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'profile_picture': None,
        'email': user.email,
        'username': user.username,
        'date_joined': user.date_joined,
        'last_login': user.last_login,
        'is_authenticated': request.user.is_authenticated,
        'is_their_profile': request.user.username == username,
    }
    return render(request, 'gallery/profile.html', context)
