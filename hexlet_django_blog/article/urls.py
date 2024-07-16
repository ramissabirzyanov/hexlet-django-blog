from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.make_redirect),
    path('<str:article_tags>/<int:article_id>/', views.IndexView.as_view(), name='article'),
]
