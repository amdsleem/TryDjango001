from django.urls import include, path
from . import views
from .views import post_list, post_create, post_detail, post_update, post_delete

app_name = 'posts'
urlpatterns = [
    path('', views.post_list, name='list'),
    path('create/', views.post_create, name='post_create'),
    path('<id>/', views.post_detail, name='detail'),
    path('<id>/edit/', views.post_update, name='update'),
    path('<id>/delete/', views.post_delete, name='post_delete'),
]
