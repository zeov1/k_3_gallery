from django.urls import path

from accounts.views import logout_view, login_view, login_done_view, signup_view, signup_done_view

urlpatterns = [
    path('login/done/', login_done_view, name='login_done'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/done/', signup_done_view, name='signup_done'),
    path('signup/', signup_view, name='signup'),
    # path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
    # path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    # path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
