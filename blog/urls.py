from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('', views.post_list, name='post_list'),
        path('posts/<str:handle>', views.view_post, name='view_post'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
