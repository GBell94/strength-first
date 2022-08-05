from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_post/', views.PostCreate.as_view(), name='add-post'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='post-detail'),
]
