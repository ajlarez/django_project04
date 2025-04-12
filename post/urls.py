from django.urls import path #CREADO PARA URLS
from post.views import PostListView, PostCreate, PostRead #CREADO PARA URLS

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'), 
    path('create/', PostCreate.as_view(), name='post_create'),
    path('detail/<int:pk>/', PostRead.as_view(), name='post_detail'), 

]