from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_post/', views.PostCreate.as_view(), name='add-post'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='post-detail'),
    path('post/edit/<int:pk>', views.PostUpdate.as_view(), name='update-post'),
    path('post/<int:pk>/delete', views.PostDelete.as_view(), name='delete-post'),
]
