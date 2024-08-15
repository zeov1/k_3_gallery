"""
URL configuration for k_3_gallery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from gallery.views import index, news, news_index, news_settings, profile, picture

urlpatterns = [
    path('', index, name='index'),
    path('news_index/', news_index, name='news_index'),
    path('news/', news, name='news'),
    path('news/settings/', news_settings, name='news_settings'),
    path('profile/<str:username>/', profile, name='profile'),
    path('picture/<int:picture_id>/', picture, name='picture'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('admin/', admin.site.urls, name='admin'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
