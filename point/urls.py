from django.urls import path,include
from django.contrib.auth import admin
from .models import User
from . import views

app_name = "point"


urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('upload/',views.PostUpload.as_view(),name='PostUpload'),
    path('<slug:slug>',views.Post.as_view(),name='post'),
]
