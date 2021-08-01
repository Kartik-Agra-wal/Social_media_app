from django.forms.models import ALL_FIELDS
from django.urls import path

from.views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeletelView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/',PostDeletelView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/comment-section/', views.comment_section, name='post-comment')
]
