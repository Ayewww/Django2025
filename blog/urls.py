from django.urls import path
from . import views
urlpatterns=[
    #    127.0.0.1:8000/blog/
    path('', views.index ),
    path('<int:pk>/', views.detail ),
    path('create/', views.create, name='blogcreate' ),
    path('createfake/', views.createfake),
    path('category/<slug>/', views.category, name='category'),
    path('<int:pk>/delete/', views.delete, name='blogdelete'),
    path('<int:pk>/update/', views.update, name='blogupdate'),
    #path('blog/{{post.pk}}/createcomment/', views.createComment, name='createcomment'),
    #path('blog/{{post.pk}}/updatecomment/', views.updateComment, name='updatecomment'),
    # 댓글 업데이트 경로
    path('blog/comment/<int:pk>/updatecomment/', views.updateComment, name='updatecomment'),
    path('blog/comment/<int:pk>/createcomment/', views.createComment, name='createcomment'),
    path('blog/comment/<int:pk>/deletecomment/', views.deleteComment, name='deletecomment'),

    
]