from django.urls import path

from accounts.views import login, logout

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='login'),
]
