from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse
from hexlet_django_blog.article.models import Article, ArticleComment
from .forms import ArticleCommentForm



class IndexView(View):


    def get(self, request, *args, **kwargs):
            articles = Article.objects.all()[:15]
            return render(request, 'articles/index.html', context={
                'articles': articles,
            })

class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })


class CommentArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        comments = ArticleComment.objects.all()
        form = ArticleCommentForm() # Создаем экземпляр нашей формы
        return render(request, 'comment.html', context={'form': form, 'article': article, 'comments':comments})
    

    def post(self, request, *args, **kwargs):
        form = ArticleCommentForm(request.POST)
        article = get_object_or_404(Article, id=kwargs['id']) # Получаем данные формы из запроса
        if form.is_valid(): # Проверяем данных формы на корректность
            form.save() # Сохраняем форму
        return redirect(reverse('article_id'))
