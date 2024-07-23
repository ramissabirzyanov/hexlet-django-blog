from django.urls import path

from hexlet_django_blog.article.views import IndexView, ArticleView, ArticleCreateView, ArticleFormEditView, ArticleFormDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='articles'),
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='article_update'),
    path('<int:id>/delete/', ArticleFormDeleteView.as_view(), name='articles_delete'),
    path('<int:id>/', ArticleView.as_view(), name='article_id'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),

]
