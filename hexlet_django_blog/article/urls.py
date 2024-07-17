from django.urls import path

from hexlet_django_blog.article.views import IndexView, ArticleView, CommentArticleView

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:id>/', ArticleView.as_view(), name='article_id'),
    path('<int:id>/', CommentArticleView.as_view(), name='comment_create'),
]
