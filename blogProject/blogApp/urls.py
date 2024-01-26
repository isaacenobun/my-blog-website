from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name = 'PostList'),
    path('<slug:slug>/', views.PostDetail.as_view(), name = 'PostDetail'),
    path('search', views.search_posts, name='search_posts')
]