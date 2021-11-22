from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete', views.del_post, name='del_post'),
    url(r'^password_change/$', views.change_password, name='change_password'),
    path('register/', views.register, name='register'),
    url(r'^accounts/reset_password/$', auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),name='reset_password'),
    url(r'^accounts/password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), name='password_reset_done'),
    url(r'^accounts/reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_complete'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), name='password_reset_confirm'),
]
