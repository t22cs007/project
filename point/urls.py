from django.urls import path,include
from django.contrib.auth import admin
from .models import User
from . import views
from .views import ItemListView

app_name = "point"


urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('create/', views.create, name='create'),
    path('success/', views.point_success, name='point_success'),
    path('upload/',views.PostUpload.as_view(),name='PostUpload'),
    #path('<slug:slug>',views.Post.as_view(),name='post'),
    path('items/', ItemListView.as_view(), name='item_list'),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:  # 開発環境でのみ有効
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)