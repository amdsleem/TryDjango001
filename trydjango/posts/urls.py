from django.urls import include, path
from . import views
from .views import post_list, post_create, post_detail, post_update, post_delete


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('detail/', views.post_detail, name='post_detail'),
    path('update/', views.post_update, name='post_update'),
    path('delete/', views.post_delete, name='post_delete'),
]
