from django.urls import path

from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('blog/<str:blog_name>/', views.blog, name='blog'),
]