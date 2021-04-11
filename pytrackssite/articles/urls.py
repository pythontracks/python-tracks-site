"""pytrackssite.articles URL Configuration
"""
from django.urls import path, include
from .views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='article-view-index'),  # Main entry into the site. Try to use <app>-<view>-<view_name> as a convention.
]
