from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from instagram.views import PostLikeToggle, PostLikeAPIToggle
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('signup/', views.signup, name='signup'),
    path('search/', views.search_profile, name='search'),
    path('account/', include('django.contrib.auth.urls')),
    path('like', views.like_post, name='like_post'),
    path('post/<id>', views.post_comment, name='comment'),
    path('follow/<to_follow>', views.follow, name='follow'),
    path('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    path('post/<id>/like', PostLikeToggle.as_view(), name='liked'),
    path('api/post/<id>/like', PostLikeAPIToggle.as_view(), name='liked-api'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='reset_password_complete'),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'), name='password')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
