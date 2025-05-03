from django.urls import path #CREADO PARA URLS
from post.views import PostListView, PostCreate, PostRead,PostUpdate, PostDelete #CREADO PARA URLS

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'), 
    path('post/create/', PostCreate.as_view(), name='post_create'),
    path('post/detail/<int:pk>/', PostRead.as_view(), name='post_detail'), 
    path('post/detail/<int:pk>/update', PostUpdate.as_view(), name='post_update'), 
    path('post/detail/<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    
]
