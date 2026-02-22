from django.urls import path
from . import views 

urlpatterns = [
        path('', views.post_list, name='post_list'),
        path('posts/<str:handle>', views.view_post, name='view_post'),
]
