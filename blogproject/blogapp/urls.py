from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:blog_id>', views.detail, name = 'detail'),
    path('new', views.new, name = 'new'),
    path('create', views.create, name = 'create'),
    path('<int:blog_id>/delete', views.delete, name = 'delete'),
]