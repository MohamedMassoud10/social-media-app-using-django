from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('signin/', views.signin, name='signin'),
    path('settings',views.setting,name='settings'),
    path('logout',views.logout,name='logout'),
    path('upload',views.upload,name='upload'),
    path('profile/<str:pk>',views.profile,name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('add_comment',views.add_comment,name='add_comment'),
]
