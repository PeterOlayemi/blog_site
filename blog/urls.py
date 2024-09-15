from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('articles/<category>/', ArticleCategoryList.as_view(), name='article_category_list'),
    path('user/profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('user/profile/update/', UserUpdateView.as_view(), name='user_update'),
    path('password/change/', ChangePasswordView.as_view(), name='change_password'),
    path('article/create/', ArticleCreateView.as_view(), name='article_create'),
    path('article/detail/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/like/<int:pk>/', ArticleLikeView.as_view(), name='article_like'),
    path('article/delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/update/<int:pk>/', ArticleUpdateView.as_view(), name='article_update'),
    path('comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/update/<int:pk>/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/reply/<int:pk>/', ReplyCommentView.as_view(), name='reply_comment'),
]
