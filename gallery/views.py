from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import NewsSettingsForm, ImageForm, EditImageCaptionForm
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

    order_by = request.GET.get('sort', 'date')
    queryset = Image.objects
    if order_by == 'date':
        queryset = queryset.order_by('date', 'time')
    elif order_by == 'publisher':
        queryset = queryset.order_by('author')
    else:
        return HttpResponseBadRequest(f'The posts can be ordered only by date or publisher!')

    first_post_number = show_posts * (page_number - 1)

    length = len(queryset)
    max_page = (length + show_posts - 1) // show_posts

    context = {
        'images': queryset[::-1][first_post_number:show_posts + first_post_number],
        'max_page': max_page,
        'page': page_number,
        'show': show_posts,
        'sort': order_by,
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
        'sort': 'date',
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
        'is_their_profile': request.user.username == username,
    }
    return render(request, 'gallery/profile.html', context)


def picture(request, picture_id):
    image_object = get_object_or_404(Image, pk=picture_id)
    return render(request, 'gallery/picture.html', {
        'image_object': image_object,
    })


def picture_upload(request):
    if request.user.is_authenticated:
        return render(request, 'gallery/picture_upload.html', {
            'form': ImageForm,
        })
    else:
        return redirect('login')


def picture_upload_done(request):
    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid() and request.user.is_authenticated:
        img = form.save(commit=False)
        img.author = request.user
        img.save()
        return redirect('news_index')
    else:
        return redirect('picture_upload')


def picture_delete(request, picture_id):
    img = get_object_or_404(Image, pk=picture_id)
    if request.user == img.author or request.user.is_superuser:
        img.delete()
    return redirect('news_index')


def picture_edit(request, picture_id):
    img = get_object_or_404(Image, pk=picture_id)
    if request.user == img.author or request.user.is_superuser:
        return render(request, 'gallery/picture_edit.html', {
            'image_object': img,
        })


def picture_edit_done(request, picture_id):
    if request.method == 'POST':
        img = get_object_or_404(Image, pk=picture_id)
        if request.user == img.author or request.user.is_superuser:
            form = EditImageCaptionForm(request.POST or None, instance=img)
            if form.is_valid():
                form.save()
                return redirect('picture', picture_id=img.id)
    return redirect('news_index')
