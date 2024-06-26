from django.contrib import admin
from django.urls import path
from main import views

#url path finder

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('sign-up', views.sign_up, name="sign_up"),
    path('create-post', views.create_post, name="create_post"),
    path('my-profile', views.my_profile, name="profile_view"),
    path('profile/<int:id>', views.profile_view, name="profile"),
    path('delete', views.delete_user, name="delete"),
    path('view-post/<int:post_id>', views.view_post, name="view-post"),
    path('follow/<int:id>', views.follow, name="follows"),
]


