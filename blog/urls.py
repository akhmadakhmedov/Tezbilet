from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('create/', index, name='index'),
    path("", articles, name='articles'),
    path("dashboard/", dashboard, name='dashboard'),
    path("addarticle/", addArticle, name='addarticle'),
    path("blog/<int:id>", detail, name='detail'),
    path('update/<int:id>', updateArticle, name='update'),
    path('delete/<int:id>', deleteArticle, name='delete'),
    path('comment/<int:id>', addComment, name='comment'),

]