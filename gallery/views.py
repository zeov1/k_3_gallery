from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import NewsSettingsForm
from .models import Image
from .tools import redirect_params


def index(request):
    return redirect('news_index')


def news(request):
    page_number = request.GET.get('page', 1)
    try:
        page_number = int(page_number)
    except ValueError:
        return HttpResponseBadRequest(f'Page {page_number} does not exist!')
    if page_number < 1:
        page_number = 1

    show_posts = request.GET.get('show', 15)
    try:
        show_posts = int(show_posts)
    except ValueError:
        return HttpResponseBadRequest(
            f'The number of posts must be integer. The number from your request: {show_posts}.')
    if show_posts < 1:
        return HttpResponseBadRequest(f'Can\'t show {show_posts} posts. The number of posts must be at least 1!')

    first_post_number = show_posts * (page_number - 1)
    queryset = Image.objects.all()

    length = len(queryset)
    max_page = (length + show_posts) // show_posts

    context = {
        'images': queryset[::-1][first_post_number:show_posts + first_post_number],
        'max_page': max_page,
        'page': page_number,
        'show': show_posts,
    }

    if page_number > 1:
        context['prev_page'] = page_number - 1
    if page_number < max_page:
        context['next_page'] = page_number + 1

    return render(request, 'gallery/news.html', context)


def news_index(request):
    return redirect_params('news', {
        'page': 1,
        'show': 15,
    })


def news_settings(request):
    return render(request, 'gallery/news_settings.html', {
        'form': NewsSettingsForm(),
    })


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
